# test for the module to load the meteo data

from osem.access_data import Meteo
import numpy as np

meteo = Meteo()
assert(meteo.get_closest_station('precipitation',
                                 coordinates=[710512, 259825],
                                 altitude=None,
                                 max_alt_diff=None)['station_name'] == 'Aadorf / Tänikon')

assert(meteo.get_meteo_data_annual('precipitation', station='Aadorf / Tänikon') == 1184.2)
assert(meteo.get_meteo_data_annual('precipitation', station='Aadorf/ Tän') == 1184.2)

assert(meteo.get_meteo_data_monthly('precipitation', station='Aadorf / Tänikon', months=['january'])[0] == 76.5)
assert(meteo.get_meteo_data_monthly('precipitation', station='Aadorf / Tänikon', months=[0, 1])[1] == 73.0)
assert(meteo.get_meteo_data_monthly('precipitation', station='Aadorf / Tänikon', months= [0, 1,2,3,4,5,6,7,8,9,10])[1] == 73.0)
assert(meteo.get_unit('precipitation') == 'millimètre')

