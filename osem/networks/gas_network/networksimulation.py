import fluids
import numpy as np
import networkx as nx
import operator
from thermo.chemical import Chemical
from scipy.linalg import qr
import fluids.vectorized as fvec
from scipy.optimize import minimize
from scipy.sparse.linalg import lsqr
from numpy.linalg import pinv


class SimulationNetwork():

    def __init__(self, net):

        # the network which will be simulation
        self.net = net

        # the result for each component of the netwrok for this pressure level
        self.bus_level = None
        self.feeder_level = None
        self.station_level = None
        self.load_level = None

        # the total amount of the load
        self.total_load = 0
        # the level which is simulated now
        self.level = None
        # the index where the feeder are
        self.ind_feeder = []

        # all the matrix to be solved
        self.i_mat = None   # the basic one
        self.mat_mass = None  # the one for the mass equation
        self.mat_pres = None # the one for the pressure
        self.z_i_mat = None # null space of the mass equation

        self.pa_to_bar = 1e-5
        self.res_check = 0  # the error on the pressure matrix

    def run_sim_by_level(self, level):
        """
        computes the gas simulation for one pressure level.

        :param level: the considered pressure level
        :return: a pandasgas network
        """


        # gas parameter
        self.level = level
        level_value = self.net.levels[level]
        fluid_type = Chemical("natural gas", T=self.net.temperature, P=level_value * self.net.corr_pnom + self.net.p_atm)

        # select network component for this pressure level
        self._select_component_for_this_level()

        # get the data by edge for this level
        materials = self.net.get_data_by_edge(level, "mat")
        roughness = np.array([fluids.material_roughness(m) for m in materials])
        leng = self.net.get_data_by_edge(level, "L_m")
        diam = self.net.get_data_by_edge(level, "D_m")

        # add load (with the load linked to a station of a lower pressure level) and give these masses to the nodes
        self._scaled_loads()
        m_dot_nodes = self._create_node_mass()

        # compute incidence matrix (so a matrix which says which node are connected to which edge)
        self._compute_i_mat()
        row0 = self.i_mat.shape[0]
        col0 = self.i_mat.shape[1]
        if self.net.solver_option['disp']:
            print('incidence matrix: done.')

        # modify i_mat so that the unknown linked with the solver are on the left side of the "equation"
        self._i_mat_with_feeder()

        # get null space for the mass (so that the space with all possible solutions form the matrix)
        self._qr_null()
        nullity_mass = self.z_i_mat.shape[1]  # how many freedom degrees

        # get one solution to the equation representing mass conservation
        res = lsqr(self.mat_mass, m_dot_nodes,
                   atol=self.net.solver_option['tol_mat_mass'],
                   btol=self.net.solver_option['tol_mat_mass'])
        sol0 = res[0]
        if self.net.solver_option['disp']:
            print('find null space for the mass equation: done.')

        # obtain the pseudo inverse matrix for the pressure equation (so the matrix which find the closest solution)
        self._i_mat_for_pressure()
        pinv_pres = pinv(self.mat_pres)
        p_noms = [level_value] * len(self.ind_feeder)
        if self.net.solver_option['disp']:
            print('find pseudo-inverse matrix for the pressure equation: done.')

        # if we have more than one possibility as solution, minimize
        if nullity_mass > 0:
            m0 = np.random.rand(nullity_mass)
            args_mass = (self.z_i_mat, sol0, self.net.v_max, diam, row0, col0, leng, roughness, fluid_type,
                         pinv_pres, p_noms, self.mat_pres, self.mat_mass, m_dot_nodes,self.net.solver_option)
            options = {'maxiter': self.net.solver_option['maxiter'], 'disp': self.net.solver_option['disp']}
            _compute_mass_and_pres.niter = 0  # attach a variable to a function

            # As we have more than on solution for the masss equation, we test many of them to find the one choice
            #  which fits the pressure equation.
            res = minimize(_compute_mass_and_pres, m0, method='SLSQP', args=args_mass, options=options)
            # all solution are the  "basic" solution + residual, cf. linear algebra.
            sol = sol0 + self.z_i_mat.dot(res.x)
        else:
            sol = sol0

        # separate the result
        m_dot_pipes = sol[:col0]
        m_dot_nodes[self.ind_feeder] = sol[col0:]

        # compute load and velocity
        v, load_pipes = self._v_from_m_dot(diam, m_dot_pipes, fluid_type)

        # compute pressure
        p_loss = _dp_from_m_dot_vec(m_dot_pipes, leng, diam, roughness, fluid_type) * (-1)
        p_loss = np.append(p_loss, p_noms)
        p_nodes = pinv_pres.dot(p_loss)
        if nullity_mass > 0 and self.net.solver_option['disp']:
            _print_minimize_state(p_nodes, res.fun, _compute_mass_and_pres.niter)

        # transfer output to self.net
        self._transfer_output_to_net(p_nodes, m_dot_nodes, v, load_pipes, m_dot_pipes)

    def _select_component_for_this_level(self):
        """
        Select the network components (pipe, bus, etc.) for this pressure level
        """

        self.bus_level = self.net.bus.loc[self.net.bus['level'] == self.level, :]
        self.feeder_level = self.net.feeder.loc[self.net.feeder["bus"].isin(self.bus_level.index), :]
        self.station_level = self.net.station.loc[self.net.station["bus_low"].isin(self.bus_level.index), :]
        self.load_level = self.net.load.loc[self.net.load["bus"].isin(self.bus_level.index), :]

    def _scaled_loads(self):
        """
        This function passes the loads from kW to kg/s using the LHV parameter and add the load linked
        to the station of the lower pressure network
        """

        # pass from kWh to kg/sec
        self.load_level.loc[:, 'load_kg_s'] = \
            (self.load_level.loc[:, "scaling"] * self.load_level.loc[:, "p_kW"]) / self.net.lhv

        # add load from the stations
        for _, row in self.net.res_station.iterrows():
            bushigh = self.net.station.at[row.name, "bus_high"]
            if self.net.bus.loc[bushigh, "level"] == self.level:
                self.load_level.loc[bushigh, 'load_kg_s'] = abs(round(row[0], self.net.solver_option['round_num']))

        self.total_loads = sum(self.load_level["load_kg_s"])

    def _create_node_mass(self):
        """
        This function create the mass for the node and add nan if the mass is to be found (feeder).
        It also return the index where the feeder/station is and the sum of the load
        """

        netnx = self.net.netnx_all[self.level]
        m_dot_nodes = np.zeros(len(netnx.nodes))
        ind_feeder = []
        for i, b in enumerate(netnx.nodes):
            if b in self.bus_level.index:
                if self.bus_level.loc[b, "type"] == "SINK":
                    m_dot_nodes[i] = self.load_level.loc[self.load_level['bus'] == b, 'load_kg_s'].values[0]
                elif self.bus_level.loc[b, "type"] == "NODE":
                    m_dot_nodes[i] = 0
                elif self.bus_level.loc[b, "type"] == "SRCE":
                    m_dot_nodes[i] = 0
                    ind_feeder.append(i)

        self.ind_feeder = np.array(ind_feeder)
        return m_dot_nodes

    def _compute_i_mat(self):
        """
        the incidence matrix of the gas network for this pressure level

        :param graph: a networkx graphc
        """

        netnx = self.net.netnx_all[self.level]
        self.i_mat = np.asarray(nx.incidence_matrix(netnx, oriented=True).todense())

    def _i_mat_with_feeder(self):
        """
        This function modify i_mat so that all the unknown are on the left side of the equation.
        So at first we have Ax = b where b are the load. We known the loads apart from the loads in the feeder. Let separe
        b in to b0 (the usual load) and bf the load from the feeder. So we have Ax-bf = b0. Now, bf is in fact more unknown.
        So let's find a matrix B so that Bx'=b0 where x' is the concatenation of x and bf. B has len(bf) more column than
        A. The value at the added column i is the values bf[i].

        We than add one equation to ensure that the total loads is equal to the mass enterting the feeder

        """

        # orginal size of incidence matrix
        row0 = self.i_mat.shape[0]
        col0 = self.i_mat.shape[1]
        self.mat_mass = self.i_mat.copy()

        # add extra empty column to B
        nb_feeder = len(self.ind_feeder)
        null_mat = np.zeros((row0, nb_feeder))
        self.mat_mass = np.append(self.mat_mass, null_mat, axis=1)

        # if a feeder is present at this line,  add a minus one to account fo rit
        for i, f in enumerate(self.ind_feeder):
            self.mat_mass[f, col0 + i] = -1

    def _qr_null(self, tol=None):
        """
        Computes the null space of A using a rank-revealing QR decomposition. This is a ready made function
        from another project"""
        Q, R, P = qr(self.mat_mass.T, mode='full', pivoting=True)
        tol = np.finfo(R.dtype).eps if tol is None else tol
        rnk = min(self.mat_mass.shape) - np.abs(np.diag(R))[::-1].searchsorted(tol)
        self.z_i_mat = Q[:, rnk:].conj()

    def _i_mat_for_pressure(self):
        """
        This function add to the matrix representing the equations of the pressure (saying that the pressure loss
        is equal to the pressure difference between two nodes) the "equations" saying that the feeder is at the nominal
        pressure.
        """
        self.mat_pres = self.i_mat.T

        # add equation saying that the pressure at the feeder is the nominal pressure (p_feeder0)
        feeder_equ = np.zeros((1, self.mat_pres.shape[1]))
        for i, f in enumerate(self.ind_feeder):
            feeder_equ2 = np.copy(feeder_equ)
            feeder_equ2[0, f] = 1
            self.mat_pres = np.append(self.mat_pres, feeder_equ2, axis=0)

    def _v_from_m_dot(self, diameter, m_dot, fluid):
        """
        get the velocity and the load in the pipe (load in %). The load is percentage of the maximum velocity.
        :param diameter: the diamter of the pipe
        :param m_dot: the mass in the pipe
        :param fluid: the characterisitc of the fluid
        :return: the velocity and the load in the pipe
        """
        q = m_dot / fluid.rho
        a = np.pi * diameter ** 2 / 4
        v = q / a
        return v, abs(100 * v / self.net.v_max)

    def _transfer_output_to_net(self, p_nodes, m_dot_nodes, v, load_pipes, m_dot_pipes):
        """
        Takes the output from the minimization and pass this result to the self.net object
        :param p_nodes: the pressure at the nodes
        :param m_dot_nodes: the toital mass passing through each nodes
        :param v: the velocity in each pipes
        :param load_pipes: the load of each pipe (in % of the maximum velcity)
        :param m_dot_pipes: mass in each nodes
        """
        # get the form of the netwrok
        r_num = self.net.solver_option['round_num']
        netnx = self.net.netnx_all[self.level]
        netnx_node = list(netnx.node)
        p_names = self.net.get_data_by_edge(self.level, 'name')

        # output bus
        self.net.res_bus.loc[netnx_node, "p_Pa"] = np.round(p_nodes, r_num)
        self.net.res_bus.loc[netnx_node, "p_bar"] = np.round(p_nodes * self.pa_to_bar, r_num)
        self.net.res_bus.loc[netnx_node, "m_dot_kg/s"] = np.round(m_dot_nodes, r_num)
        self.net.res_bus.loc[netnx_node, "p_kW"] = np.round(m_dot_nodes * self.net.lhv, r_num)

        # output pipe
        self.net.res_pipe.loc[p_names, "m_dot_kg/s"] = np.round(m_dot_pipes, r_num)
        self.net.res_pipe.loc[p_names, "p_kW"] = np.round(m_dot_pipes * self.net.lhv, r_num)
        self.net.res_pipe.loc[p_names, "v_m/s"] = np.round(v, r_num)
        self.net.res_pipe.loc[p_names, "loading_%"] = np.round(load_pipes, r_num)

        # output feeder
        f_names = self.feeder_level.index
        self.net.res_feeder.loc[f_names, "m_dot_kg/s"] = self.net.res_bus.loc[
            self.feeder_level["bus"].values, "m_dot_kg/s"].values
        self.net.res_feeder.loc[f_names, "p_kW"] = self.net.res_bus.loc[self.feeder_level["bus"].values, "p_kW"].values
        loading_feeder = np.abs(
            100 * self.net.res_feeder.loc[f_names, "p_kW"] / self.net.feeder.loc[f_names, "p_lim_kW"])
        loading_feeder = loading_feeder.astype(float)
        self.net.res_feeder.loc[f_names, "loading_%"] = np.round(loading_feeder.values, r_num)

        # output station
        s_names = self.station_level.index
        self.net.res_station.loc[s_names, "m_dot_kg/s"] = self.net.res_bus.loc[
            self.station_level["bus_low"].values, "m_dot_kg/s"].values
        self.net.res_station.loc[s_names, "p_kW"] = self.net.res_bus.loc[
            self.station_level["bus_low"].values, "p_kW"].values
        loading_station = np.abs(
            100 * self.net.res_station.loc[s_names, "p_kW"] / self.net.station.loc[
                self.station_level.index, "p_lim_kW"])
        loading_station = loading_station.astype(float)
        self.net.res_station.loc[s_names, "loading_%"] = np.round(loading_station.values, r_num)

    def multiply_pressure_matrix_to_check(self):

        self.res_check = 0

        # check for pressure conservation for each level
        sorted_levels = sorted(self.net.levels.items(), key=operator.itemgetter(1))
        for level, value in sorted_levels:
            if level in self.net.bus["level"].unique():

                # get network
                self.level = level
                netnx = self.net.netnx_all[level]
                level_value = self.net.levels[level]
                fluid_type = Chemical("natural gas", T=self.net.temperature, P=level_value + self.net.p_atm)

                # get network component for this level (not all component just part of it)
                self._compute_i_mat()
                self.bus_level = self.net.bus.loc[self.net.bus['level'] == level, :]
                self.load_level = self.net.load.loc[self.net.load["bus"].isin(self.bus_level.index), :]
                self._scaled_loads()
                self._create_node_mass()

                # get data for this level
                materials = self.net.get_data_by_edge(level, "mat")
                roughness = np.array([fluids.material_roughness(m) for m in materials])
                leng = self.net.get_data_by_edge(level, "L_m")
                diam = self.net.get_data_by_edge(level, "D_m")
                name_pipe = self.net.get_data_by_edge(level, "name")
                m_dot_pipes = self.net.res_pipe.loc[name_pipe, "m_dot_kg/s"].values
                p_nodes = self.net.res_bus.loc[np.array(netnx.nodes), "p_Pa"].values

                # make the matrix multiplication (should be null)
                self._i_mat_for_pressure()
                p_loss = _dp_from_m_dot_vec(m_dot_pipes, leng, diam, roughness, fluid_type) * (-1)
                p_loss = np.append(p_loss, [level_value] * len(self.ind_feeder))
                self.res_check += sum(self.mat_pres.dot(p_nodes) - p_loss)


def _compute_mass_and_pres(m0, *args):
    """
    This function computes the mass, knowing a first solution to the equation and the null of the modified incidence
    maxtrix. It returns the rest of the pressure loss which is minimized. It can not easily be a method of a function
    as it is called by minimize from scipy.

    """

    z_i_mat, sol1, v_max, diam, row0, col0, leng, roughness, fluid_type, pinv_pres, p_noms, mat_pres, mat_all, \
    m_dot_nodes, solver_option = args

    # get new solution from "basic" solution
    m_here = sol1 + z_i_mat.dot(m0)
    m_here = m_here[:col0]

    # loss of pressure in each pipes
    p_loss = _dp_from_m_dot_vec(m_here, leng, diam, roughness, fluid_type) * (-1)
    p_loss = np.append(p_loss, p_noms)

    # equations for the pressure (should be zero, so minize residual)
    p_nodes = pinv_pres.dot(p_loss)
    residual = np.sum(np.abs(mat_pres.dot(p_nodes) - p_loss))

    if solver_option['disp'] and _compute_mass_and_pres.niter % solver_option['iter_print'] == 0:
        _print_minimize_state(p_nodes, residual, _compute_mass_and_pres.niter)
    _compute_mass_and_pres.niter += 1

    return residual


def _dp_from_m_dot_vec(m_dot, l, d, e, fluid):
    """
    Compute pressure loss using fluids library. Called by  _compute_mass_and_pres.
    """
    a = np.pi * (d / 2) ** 2
    v = (m_dot / fluid.rho) / a
    v[v==0] = 1e-7
    re = fvec.core.Reynolds(v, d, fluid.rho, fluid.mu)
    fd = fvec.friction_factor(re, eD=e / d)
    k = fvec.K_from_f(fd=fd, L=l, D=d)
    return fvec.dP_from_K(k, rho=fluid.rho, V=v)


def _print_minimize_state(p_nodes, residual, iter):
    """
    This function print the current state of the minimization for the pressure equation.
    Called by _compute_mass_and_pres.

    :param p_nodes: the pressure in the nodes
    :param residual: the resiudal of the pressure equation
    :param iter: the current iteration
    """
    print('----------------------------------------------------------------------')
    print('Current State for the Minimization for Iteration ' + str(iter))
    print("The current pressure minimum: " + str(np.min(p_nodes)))
    print("The current pressure maximum: " + str(np.max(p_nodes)))
    print("The current pressure mean: " + str(np.mean(p_nodes)))
    print("The current residual is : " + str(residual))



