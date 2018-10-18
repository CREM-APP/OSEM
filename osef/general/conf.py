# this is the configuration file for OSEM
import os

############################################################
# default variables for all the modules
data_folder = "data"
data_folder = r'W:\Enerapi\code\OSEF\data'
cutoff = 0.45  # used to compare string, 1 is a perfect match on the string, with 0 all string match.

##############################################################
# default variables for the acesss data feature

# kbob
version_default = '2016'
data_folder_kbob = os.path.join(data_folder, 'data_kbob')
basename_unit = "kbob_unit"  # filename for the unit file: basename + version +'.csv'
basename_kbob = "kbob_data"  # filename for the kbob file: basename + version +'.csv'
filename_trans_ind = "kbob_translation_indicator.csv"   # name of the file with the translation data

# political objectives
basename_pol = "political_obj.csv"
column_not_print_pol = ['reference_year', 'objective_year', 'note', 'reference']  # columns which are not objectives

# price
precision_price = 5  # to which precision the price in CHF must be calculated
basename_price = "price_database.db"
name_tableunit = 'UNIT_TECHNO'
column_not_print_price = ["units", "reference", "note"]  # columns which are not a type of price
ref_col = "reference"
myind = "myind"
nb_point_graph = 50
interp_lim = 0.3
warning_ignore = '.*Covariance of the parameters could not be estimated.*'
opex_name = 'maintenance'

# kpi
temp_building = [[50, 25, 25], [70, 60, 50]]  # # [[%percent building], [temperature]]
filename_eff = 'kpi_efficiency_heating.csv'
temp_ext = 22  # exterior temperature °C

# meteo data
data_folder_meteo = os.path.join(data_folder, 'data_meteo_swiss')
filenames = [i for i in os.listdir(data_folder_meteo) if i != 'data_source.txt']
nbline_header = 8

###############################################################
# defalut value for the plot

# plot kpi
xlabel = 'Years'
ylabelco2 = 'CO$_{2}$ emission [kg]'
ylabelfinal = 'Final Energy [kWh]'
ylabelprimary = 'Primary Energy [kWh]'
ylabelrenew = 'Primary Energy [kWh]'
renew_colname = ['years', 'scenarios','renewable', 'non-renewable']
fontsize =12
width = 0.2
figsize = (8,8)


#############################################################