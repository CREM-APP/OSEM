import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey as SankeyMatplotlib
import numpy as np
import osef.general.conf as conf


class Sankey:
    """
    This class manage and plot the Sankey plot
    """

    def __init__(self):
        pass

    def plot_sankey(self, values_flows, connect, title='', show=True):
        """
        This method call the Sankey function of matplotlib to plot a Sankey. For the variable connect, the key is the
        start of the flow and the value is the end of the flow

        Example:
        values_flows = {'ini1':1000, 'ini2':3000, 'mid1': 200, 'mid2': 5000, 'out1': 1500, 'out2':1500}
        connect =  [('ini1', 'mid1'),
                    ('ini1', 'mid2'),
                    ('ini2', 'mid2'),
                    ('mid1', 'end1'),
                    ('mid1', 'end2'),
                    ('mid2', 'end2')]

        :param values_flows: a dict with the name and the value of each flows
        :param connect: a  list of tuble (start, end) describing the connection using the same labels as values_flows
        :param title: A string which is the title of the figure
        :param show: If True the figure is shown otherwise not
        """
        # start Sankey plot
        sankey = SankeyMatplotlib()
        plt.title(title)

        # get the flow which are the start of the graphic(level0)
        start_value = [k[0] for k in connect]
        end_value = [k[1] for k in connect]
        level_ind = [ind for ind, s in enumerate(start_value) if s not in end_value]

        # make one Sankey by level
        prior = -1
        while len(level_ind) > 0 and prior < 200:

            # get label of the flows at this level
            label_in = [c[0] for ind, c in enumerate(connect) if ind in level_ind]
            label_in = list(np.unique(np.array(label_in)))
            label_out = [c[1] for ind, c in enumerate(connect) if ind in level_ind]
            label_out = list(np.unique(np.array(label_out)))
            label_level =label_in+label_out

            # get flow at this level
            flow_in = [values_flows[la] for la in label_in]
            flow_out = [-values_flows[la] for la in label_out]
            flow_level = flow_in + flow_out

            # get new level in
            level_ind = [ind for ind, s in enumerate(start_value) if s in label_out]

            # get orientation - can be 1,0,-1
            # says if an arrow is coming from the top or bottom of the plot
            nb_flow = len(label_level)
            orientations = np.zeros((nb_flow,))
            if prior == -1:
                orientations[:len(label_in)] = 1
            if len(level_ind) == 0:
                orientations[len(label_in):] = -1

            print(label_level)
            print(flow_level)

            # plot
            if prior < 0:
                sankey.add(flows=flow_level,
                           labels=label_level,
                           orientations=orientations)
            else:
                pass
                # sankey.add(flows=flow_level,
                #            labels=label_level,
                #            orientations=orientations,
                #            prior=prior,
                #            connect = (3,1))  # (2,0)


            # ind of the graph
            prior +=1

        # finish plot
        sankey.finish()
        if show:
            plt.show()

values_flows = {'ini1':1000, 'ini2':2000, 'mid1': 800, 'mid2': 2200, 'out1': 1000, 'out2':2000}
connect = {('ini1', 'mid1') : 1000,
           ('ini1', 'mid2') : 2000,
           ('ini2', 'mid2'),
           ('mid2', 'out2'),
           ('mid2', 'out1'),
           ('mid1', 'out1')}
mysankey = Sankey()
mysankey.plot_sankey(values_flows, connect, title='', show=True)
