"""
This class plot different kpi
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import osem.general.conf as conf
from osem.access_data import kpi


class PlotKpi:
    
    def __init__(self):

        self.mykpi = kpi.Kpi()

        # parameter for the plot
        self.opt_plot = conf.opt_plot

    def plot_c02(self, data_kpi, fig_name, title_name='', ylabel=conf.ylabelco2, color=None, xlabel=None,
                 fontsize=None, width=None, figsize=None, tech_name_for_plot=None, show=True):
        """
        This function creates a stacked bar plot with bar grouped by scenarios for different years. It is used to plot
        c02 emission.
    
        It needs a pandas dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        The value in the dataframe are the useful energy
    
        :param data_kpi: the data for useful energy as described above.
        :param fig_name: the name of the figure (with path if necessary)
        :param ylabel: the label for the y-axis (depends on the kpi plotted)
        :param color: the color of the plot (must be of of len > number of technology)
        :param title_name: the title of the plot
        :param xlabel: the label for the xaxis
        :param fontsize: the size of the font
        :param width: the width of the bar
        :param tech_name_for_plot: Usually the name on the plot are the title of the excel column, it can be
               changed here in case of
        :param figsize: the size of the figure (height,length)
        :param show: If True the figure is shown otherwise not
        """
    
        # compute value
        co2emission = self.mykpi.get_co2_emission(data_kpi)

        # change plot parameter
        self._set_plot_param(title_name, ylabel, color, xlabel, fontsize, width, figsize, tech_name_for_plot)
    
        # create figure only for present situation
        if len(data_kpi) == 1:
            self._present_kpi_plot(co2emission, fig_name, show)
        # create figure for various scenarios
        else:
            self._scenarios_kpi_plot(co2emission, fig_name, show)

    def plot_final_energy(self, data_kpi, fig_name, title_name='', ylabel=conf.ylabelfinal, color=None,
                          xlabel=None, fontsize=None, width=None, figsize=None, tech_name_for_plot=None, show=True):
        """
        This function creates a stacked bar plot with bar grouped by scenarios for different years. It is used to plot
        the final energy.

        It needs a pandas dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        The value in the dataframe are the useful energy.
    
        :param data_kpi: the data for useful energy as described above.
        :param fig_name: the name of the figure (with path if necessary)
        :param ylabel: the label for the y-axis (depends on the kpi plotted)
        :param color: the color of the plot (must be of of len > number of technology)
        :param title_name: the title of the plot
        :param xlabel: the label for the xaxis
        :param fontsize: the size of the font
        :param width: the width of the bar
        :param figsize: the size of the figure (height,length)
        :param tech_name_for_plot: Usually the name on the plot are the title of the excel column, it can be
               changed here in case of
        :param show: If True the figure is shown otherwise not
            """
    
        # compute value
        final_energy = self.mykpi.get_energy_final(data_kpi)

        # change plot parameter
        self._set_plot_param(title_name, ylabel, color, xlabel, fontsize, width, figsize, tech_name_for_plot)

        # create figure only for present situation
        if len(data_kpi) == 1:
            self._present_kpi_plot(final_energy, fig_name, show)
        # create figure for various scenarios
        else:
            self._scenarios_kpi_plot(final_energy, fig_name, show)

    def plot_primary_energy(self, data_kpi, fig_name, title_name='', ylabel=conf.ylabelprimary, color=None,
                            xlabel=None, fontsize=None, width=None, figsize=None, tech_name_for_plot=None, show=True):
        """
        This function creates a stacked bar plot with bar grouped by scenarios for different years. It is used to plot
        primary energy.
    
        It needs a pandas dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        The value in the dataframe are the useful energy.
    
        :param data_kpi: the data for useful energy as described above.
        :param fig_name: the name of the figure (with path if necessary)
        :param ylabel: the label for the y-axis (depends on the kpi plotted)
        :param color: the color of the plot (must be of of len > number of technology)
        :param title_name: the title of the plot
        :param xlabel: the label for the xaxis
        :param fontsize: the size of the font
        :param width: the width of the bar
        :param figsize: the size of the figure (height,length)
        :param tech_name_for_plot: Usually the name on the plot are the title of the excel column, it can be
               changed here in case of
        :param show: If True the figure is shown otherwise not
        """
        # compute value
        primary_energy = self.mykpi.get_energy_primary(data_kpi)

        # change plot parameter
        self._set_plot_param(title_name, ylabel, color, xlabel, fontsize, width, figsize, tech_name_for_plot)

        # create figure only for present situation
        if len(data_kpi) == 1:
            self._present_kpi_plot(primary_energy, fig_name, show)
        # create figure for various scenarios
        else:
            self._scenarios_kpi_plot(primary_energy, fig_name, show)

    def plot_renewable_energy(self, data_kpi, fig_name, title_name='', ylabel=conf.ylabelrenew, color=None,
                              xlabel=None, fontsize=None, width=None, figsize=None, tech_name_for_plot= None,
                              show=True):
        """
        This function creates a stacked bar plot with bar grouped by scenarios for different years. It is used to plot
        primary emission.
    
        It needs a pandas dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        The value in the dataframe are the kpi which needs plotting.
    
        :param data_kpi: the data for useful energy as described above.
        :param fig_name: the name of the figure (with path if necessary)
        :param ylabel: the label for the y-axis (depends on the kpi plotted)
        :param color: the color of the plot (must be of of len > number of technology)
        :param title_name: the title of the plot
        :param xlabel: the label for the xaxis
        :param fontsize: the size of the font
        :param width: the width of the bar
        :param figsize: the size of the figure (height,length)
        :param tech_name_for_plot: Usually the name on the plot are the title of the excel column, it can be
               changed here in case of
        :param show: If True the figure is shown otherwise not
        """
        # create renewable dataframe
        renew_out = pd.DataFrame(0, index=data_kpi.index, columns=conf.renew_colname)
        renew_out['years'] = data_kpi['years']
        renew_out['scenarios'] = data_kpi['scenarios']
    
        # compute value
        primary_energy = self.mykpi.get_energy_primary(data_kpi).iloc[:,2:]
        renew_data = self.mykpi.get_renewable_part(data_kpi).iloc[:,2:]
    
        # sum for all tech and spearate between renew and not renew
        renew_data = renew_data.sum(axis=1)
        primary_energy = primary_energy.sum(axis=1)
        renew_out.iloc[:, 2] = renew_data
        renew_out.iloc[:, 3] = primary_energy - renew_data

        # change plot parameter
        self._set_plot_param(title_name, ylabel, color, xlabel, fontsize, width, figsize, tech_name_for_plot)

        # create figure only for present situation
        if len(data_kpi) == 1:
            self._present_kpi_plot(renew_out, fig_name, show)
        # create figure for various scenarios
        else:
            self._scenarios_kpi_plot(renew_out, fig_name, show)

    def _present_kpi_plot(self, chosen_kpi, fig_name, show):
        """
        This function plots the kpi for the present case with only one year and one scenario.

        It needs a pandas dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        The value in the dataframe are the kpi which needs plotting. In this case, only one year and one scenarios must
        be present!

        :param chosen_kpi: the data for the kpi selected.
        :param fig_name: the name of the figure (with path if necessary)
        :param show: If True the figure is shown otherwise not

        """
        # prepare
        tech_name = chosen_kpi.columns[2:]
        data_kpi_here = chosen_kpi.iloc[0, 2:]
        year = chosen_kpi.iloc[0, 1]
        ind_for_bar_plot = list(np.arange(len(tech_name)))

        # get font size
        plt.rcParams.update({'font.size': self.opt_plot['fontsize']})

        # create figure
        plt.figure(figsize=self.opt_plot['figsize'])

        plt.bar(ind_for_bar_plot, data_kpi_here, color=self.opt_plot['color'], width=self.opt_plot['width_pres'])
        if self.opt_plot['tech_name_for_plot'] is None:
            plt.xticks(ind_for_bar_plot, tech_name)
        else:
            plt.xticks(ind_for_bar_plot, self.opt_plot['tech_name_for_plot'])
        if len(self.opt_plot['title_name']) == 0:
            plt.title('KPI for the year ' + str(year))
        else:
            plt.title(self.opt_plot['title_name'])
        plt.ylabel(self.opt_plot['ylabel'])
        plt.xlabel(self.opt_plot['xlabel_pres'])

        # show and save
        plt.savefig(fig_name)
        if show:
            plt.show()

    def _scenarios_kpi_plot(self, chosen_kpi, fig_name, show):
        """
        This function creates a stacked bar plot with bar grouped by scenarios for different years. It is used to plot
        c02 emission, final energy and so forth.
    
        It needs a pandas dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        The value in the dataframe are the kpi which needs plotting.
    
        :param chosen_kpi: the data for the chosen kpi as described above.
        :param fig_name: the name of the figure (with path if necessary)
        :param show: If True the figure is shown otherwise not
        """
    
        # manage data
        scenarios = chosen_kpi['scenarios'].unique()
        years = chosen_kpi['years'].unique()
        tech_name = chosen_kpi.columns[2:]
        year_ind = np.arange(len(years), dtype=float)
        width = self.opt_plot['width_scenario']
    
        # get color and font size
        if self.opt_plot['color'] is None:
            color = np.random.rand(len(tech_name), 3)
        else:
            color = self.opt_plot['color']
        plt.rcParams.update({'font.size': self.opt_plot['fontsize']})
    
        # check that each years is present in all scenarios
        for sce in scenarios:
            years_sce = chosen_kpi.loc[chosen_kpi['scenarios'] == sce, 'years']
            if np.any(years != years_sce.values):
                raise ValueError('Each scenarios must be computed for the same years')
    
        # create figure
        plt.figure(figsize=self.opt_plot['figsize'])
        ax1 = plt.subplot(1, 1, 1)
        plt.title(self.opt_plot['title_name'])
        plt.ylabel(self.opt_plot['ylabel'])
    
        # position axis ticks
        pos_year = year_ind + (width * len(scenarios)) / 2 + width / 2
        pos_sce = []
    
        # stacked bar plot
        for sce in scenarios:
            year_ind += width
            pos_sce.extend(year_ind)
            bottom_col = np.zeros(len(years))
            for i, t in enumerate(tech_name):
                data_sce_t = chosen_kpi.loc[chosen_kpi['scenarios'] == sce, t]
                if color is not None:
                    plt.bar(year_ind, data_sce_t, width=width * 0.9, color=color[i], bottom=bottom_col)
                else:
                    plt.bar(year_ind, data_sce_t, width=width * 0.9, color=color[:, i], bottom=bottom_col)
                bottom_col += data_sce_t
        if self.opt_plot['tech_name_for_plot'] is None:
            plt.legend(tech_name)
        else:
            plt.legend(self.opt_plot['tech_name_for_plot'])

        # Set second x-axis
        plt.xlim(0, len(year_ind))
        ax1.set_xticks(pos_sce)
        ax1.set_xticklabels(chosen_kpi['scenarios'], fontsize=self.opt_plot['fontsize'])
        ax2 = ax1.twiny()
        ax2.set_xticks(pos_year)
        ax2.set_xticklabels(years, fontsize=self.opt_plot['fontsize'])
        ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
        ax2.xaxis.set_label_position('bottom')
        ax2.spines['bottom'].set_position(('outward', 36))
        ax2.set_xlim(ax1.get_xlim())
        plt.xlabel(self.opt_plot['xlabel_scenario'])
        plt.xlim([0, len(year_ind)])
        bottom, top = plt.ylim()
        plt.ylim((bottom, top * 1.1))
        # plt.tight_layout()
    
        # show and save
        plt.savefig(fig_name)
        if show:
            plt.show()

    def _set_plot_param(self, title_name, ylabel, color, xlabel, fontsize, width, figsize, tech_name_for_plot):
        """
        This function set the plot parameters.

        :param title_name: name of title
        :param ylabel: the label of the y axis
        :param color: the color of the bar plot
        :param xlabel: the label of the x aaxis
        :param fontsize: the fond size
        :param width: the width of the bar
        :param figsize: the size of the figure
        :param tech_name_for_plot: Usually the name on the plot are the title of the excel column, it can be
               changed here in case of
        """

        attributes_to_be_saved = [width, width, figsize, fontsize, xlabel, xlabel, title_name, color, tech_name_for_plot]
        name_attribute = ['width_scenario', 'width_pres', 'figsize', 'fontsize', 'xlabel_pres',
                          'xlabel_scenario', 'title_name', 'color', 'tech_name_for_plot']

        for i, att in enumerate(attributes_to_be_saved):
            if att is None:
                self.opt_plot[name_attribute[i]] = conf.opt_plot[name_attribute[i]]
            else:
                self.opt_plot[name_attribute[i]] = att

        self.opt_plot['ylabel'] = ylabel