from osem.building_demand import *
from osem.distribution_network import *
from osem.energy_conversion import *
from osem.natural_resources import *





# //Building/HeatPowerSupplyTemp/calculate
print('/Building/HeatPowerSupplyTemp/calculate');
x =  {"affectation": 1, "period": 8020, "SRE": 100, "ae": 7201, "t_ext": [0]};

ret = HeatPowerSupplyTemp(x).calculate()
print('HeatPowerSupplyTemp calculate = {0}'.format(ret ))