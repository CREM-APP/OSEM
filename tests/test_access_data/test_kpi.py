import pandas as pd
import os
from osef.access_data import Kpi
import osef.general.conf as conf


filename_test = 'kpi_example_c02.xlsx'
data_heating = pd.read_excel(os.path.join(conf.data_folder, filename_test))
kpi = Kpi()
assert (kpi.get_co2_emission(data_heating, True).iloc[:, -1] == [0,0,0,125.6,138.16,150.72,125.60,138.16,150.72]).all()