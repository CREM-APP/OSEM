

from osem.distribution_network.heat_network import HeatNetwork




class TestHeatNetwork():


    def test_the_estimation_should_be_correct_case1(self):
        args = {"len_tot": 10000, "t_cons_max": 90, "p_cons_tot": 5000, "t_return_fixed": 60}

        expected = {"ratio_th_loss": 0.05, "p_supply": 5265.484, "t_reject": 60.6, "fluid_flow": 146.18}

        actual = HeatNetwork(args).calculate()


        assert expected["ratio_th_loss"] == actual["ratio_th_loss"]
        assert expected["p_supply"] == actual["p_supply"]
        assert expected["t_reject"] == actual["t_reject"]
        assert expected["fluid_flow"] == actual["fluid_flow"]

    def test_the_estimation_should_be_correct_case2(self):
        args = {"len_tot": 10000, "t_cons_max": 40, "p_cons_tot": 10000, "t_return_fixed": 20, "ground_temp": 8}

        expected = {"ratio_th_loss": 0.009, "p_supply":  10089.501}

        actual = HeatNetwork(args).calculate()
        assert expected["ratio_th_loss"] == actual["ratio_th_loss"]
        assert expected["p_supply"] == actual["p_supply"]


    def test_the_estimation_should_be_correct_case3(self):
        args = {"len_tot": 10000, "t_cons_max": 40, "p_cons_tot": 10000, "t_return_fixed": 20, "th_loss_coef": 0.5}

        expected = {"ratio_th_loss": 0.02, "p_supply": 10201}

        actual = HeatNetwork(args).calculate()

        assert expected["ratio_th_loss"] == actual["ratio_th_loss"]
        assert expected["p_supply"] == actual["p_supply"]


    def test_the_estimation_should_be_correct_case4(self):
        args = {"len_tot": 10000, "t_cons_max": 40, "p_cons_tot": 10000, "t_return_fixed": 20, "rho_fluid": 2000}

        expected = {"ratio_th_loss": 0.008, "p_supply": 10081.365}

        actual = HeatNetwork(args).calculate()

        assert expected["ratio_th_loss"] == actual["ratio_th_loss"]
        assert expected["p_supply"] == actual["p_supply"]


    def test_the_estimation_should_be_correct_case5(self):
        args = {"len_tot": 10000, "t_cons_max": 90, "p_cons_tot": 10000, "t_return_fixed": 60, "cp_mass_fluid": 4000}

        expected = {"ratio_th_loss": 0.026, "p_supply": 10264.698, "fluid_flow": 302.812}

        actual = HeatNetwork(args).calculate()

        assert expected["ratio_th_loss"] == actual["ratio_th_loss"]
        assert expected["p_supply"] == actual["p_supply"]
        assert expected["fluid_flow"] == actual["fluid_flow"]


    def test_the_estimation_should_be_correct_case6(self):
        args = {"len_tot": 10000, "t_cons_max": 90, "p_cons_tot": 10000, "t_return_fixed": 20, "v_max": 1.8}

        expected = {"ratio_th_loss": 0.018, "p_supply": 10184.005, "fluid_flow":  123.041, "inner_diameter_min": 0.155}

        actual = HeatNetwork(args).calculate()


        assert expected["ratio_th_loss"] == actual["ratio_th_loss"]
        assert expected["p_supply"] == actual["p_supply"]
        assert expected["fluid_flow"] == actual["fluid_flow"]
        assert expected["inner_diameter_min"] == actual["inner_diameter_min"]