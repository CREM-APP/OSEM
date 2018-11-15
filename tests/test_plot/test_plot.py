# this python file test the plot
import matplotlib.pyplot as plt
import pandas as pd
import os
import time

import osef.general.conf as conf
from osef.plot import plot_kpi

# load test data
filename_test = 'kpi_example_c02.xlsx'
data_kpi = pd.read_excel(os.path.join(conf.data_folder, filename_test))

# create figure in the 'fig test' directory
dirname = os.path.join('tests', 'fig_test')
plot_kpi.plot_c02(data_kpi, os.path.join(dirname, 'co2emi.png'), show=False)
plot_kpi.plot_primary_energy(data_kpi, os.path.join(dirname, 'primary.png'), show=False)
plot_kpi.plot_renewable_energy(data_kpi, os.path.join(dirname, 'renew.png'), show=False)


