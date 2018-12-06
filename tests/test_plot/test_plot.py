# this python file test the plot
import matplotlib.pyplot as plt
import pandas as pd
import os
import time

import osem.general.conf as conf
from osem.plot import plot_kpi

# load test data for the scanerios
filename_test = 'kpi_example_c02.xlsx'
data_kpi = pd.read_excel(os.path.join(conf.data_folder, filename_test), sheet_name='scenarios')

# create figure in the 'fig test' directory
dirname = os.path.join('tests', 'fig_test')
myplot = plot_kpi.PlotKpi()
myplot.plot_c02(data_kpi, os.path.join(dirname, 'co2emi.png'), show=False)
myplot.plot_primary_energy(data_kpi, os.path.join(dirname, 'primary.png'), show=False)
myplot.plot_renewable_energy(data_kpi, os.path.join(dirname, 'renew.png'), show=False)

# load test data for the present
filename_test = 'kpi_example_c02.xlsx'
data_kpi = pd.read_excel(os.path.join(conf.data_folder, filename_test), sheet_name='present')

# create figure in the 'fig test' directory
dirname = os.path.join('tests', 'fig_test')
myplot.plot_c02(data_kpi, os.path.join(dirname, 'co2emi_pres.png'), show=False)
myplot.plot_primary_energy(data_kpi, os.path.join(dirname, 'primary_pres.png'), show=False)
myplot.plot_renewable_energy(data_kpi, os.path.join(dirname, 'renew_pres.png'), show=False)