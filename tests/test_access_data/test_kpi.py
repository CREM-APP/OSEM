import pandas as pd
import os
from osem.access_data import Kpi
import osem.general.conf as conf


# load test data
filename_test = 'kpi_example_c02.xlsx'
data_heating = pd.read_excel(os.path.join(conf.data_folder, filename_test))
kpi = Kpi()

# co2
assert (kpi.get_co2_emission(data_heating).iloc[:, -1] == [0,0,0,125.6,138.16,150.72,125.60,138.16,150.72]).all()

# primary energy

assert (kpi.get_energy_primary(data_heating).iloc[:, -1] == [0,0,0,3460,3806,4152,3460,3806,4152]).all()

# renewable
assert sum(abs(kpi.get_renewable_part(data_heating).iloc[:, -1] - [0,0,0,1636,1799.6,1963.2,1636,1799.6,1963.2])) < 1e-5

# final energy
assert sum(abs(kpi.get_energy_final(data_heating).iloc[:, -1] - [0.000000,0.000000,0.000000,89.559767,
                                                                 98.515743,107.471720,89.559767,
                                                                 98.515743,107.471720])) < 1e-5


# data for price
data_heating_power = data_heating
data_heating_power.iloc[:,2:] = data_heating.iloc[:,2:]/5 + 120
data_heating_power = data_heating_power.rename(columns = {'air-water heat pump':'HeatPumpAirWater'})
print(data_heating_power)

# opex
assert sum(abs(kpi.get_opex(data_heating_power).iloc[:, -1] - [4155.767442,4155.767442,4155.767442,9702.677741,
                                                               10257.368771,10812.059801,9702.677741,10257.368771,10812.059801])) < 1e-5

#capex
assert sum(abs(kpi.get_capex(data_heating_power).iloc[:, -1] - [220656.071909, 220656.071909, 220656.071909,
                                                                605697.602522, 644201.755584, 682705.908645,
                                                                605697.602522, 644201.755584, 682705.908645])) < 1e-5

#reference
assert kpi.get_reference('co2emision') == "Friedli R., Gugerli H. «Plattform «Ökobilanzdaten im Baubereich»" \
                                   " Gründungsdokument, Coordination Group for Construction and Property Service " \
                                   "(KBOB).» 2011"
assert kpi.get_reference('CAPEX', 'BoilerOil')[400] == "Planair, Thermoreseau de SATOM SA; Comparaison de prix de " \
                                                       "chauffage,SATOM SA, 2015"


