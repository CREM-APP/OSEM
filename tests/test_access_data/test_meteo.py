# test for the meteo data


meteo = Meteo()
assert(meteo.get_closest_station('precipitation', [710512, 259825], altitude=None, max_altitude_difference=None)
       == 'Aadorf / Tänikon')

assert(meteo.get_meteo_data_annual('precipitation', 'Aadorf / Tänikon') == 1184.2)
assert(meteo.get_meteo_data_annual('precipitation', 'Aadorf/ Tän') == 1184.2)

assert(meteo.get_meteo_data_monthly('precipitation', 'Aadorf / Tänikon', ['january']) == [76.5])
assert(meteo.get_meteo_data_monthly('precipitation', 'Aadorf / Tänikon', [0, 1]) == [76.5, 73.0])
assert(meteo.get_unit('precipitation') == 'millimètre')

