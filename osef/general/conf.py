# this is the configuration file for OSEM
import os

############################################################
# default variables for all the modules
data_folder = "data"
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
warning_ignore = '.*Covariance of the parameters could not be estimated.*'

# kpi
temp_building = [[50, 25, 25], [70, 60, 45]]  # # [[%percent building], [temperature]]
filename_eff = 'kpi_efficiency_heating.csv'
temp_ext = 25  # exterior temperature °C

###############################################################
