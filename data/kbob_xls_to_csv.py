import os
import pandas as pd
import json


def xls_to_csv(filename, year, filename_trans="kbob_translation_term.csv"):
    """
    Transform the kbob data from the a xlsx file to a csv. It save the units in a separate json file.

    Because we create a csv file, the comma in the french kbob terminology (i.e., the last column of the xlsx
     file with technology names) will be transformed to a hyphen.

    Usage::
    * Load the kbob data in an Excel file. It is usually in a .zip file at the address :
    https://www.kbob.admin.ch/kbob/fr/home/publikationen/nachhaltiges-bauen/oekobilanzdaten_baubereich.html
    * Check that the downloaded kbob in in kWh and not MJ as both are available
    * use xls_to_csv("my_kbob", 2018)

    :param filename: string - the xlsx file with the kbob
    :param year: can be a int, float, or string - will be added to the name of the created csv files
    :param filename_trans: string - name of the csv file which translate kbob terminology in german, french and english
    :return: none
    """

    # name of the files to load and create
    sheetname = "Energie Energie"
    name_base_csv = "kbob_data"
    filename_unit = "kbob_unit" + str(year)+".json"

    # load kbob
    if not filename.endswith((".xls", ".xlsx", ".ods")):
        print('Error: Need an Excel file')
        return
    if os.path.isfile(filename):
        df_kbob = pd.read_excel(filename, sheet_name=sheetname, skiprows=6, usecols=[4, 5, 6, 7, 8, 9, 11])
    else:
        print('Error: File not found')
        return
    if "kWh" not in filename:
        print('Warning: The kbob loaded here should be in kWh. Please check units.')

    # rename column
    with open(filename_unit, 'r') as fp:
        col_unit = json.load(fp)
    column_name = col_unit.keys()
    df_kbob.dropna(inplace=True)
    df_kbob.columns = column_name
    df_kbob["French_Name"] = df_kbob["French_Name"].str.replace(',', ' -')

    # get index in english terminology
    trans_data = pd.read_csv(filename_trans, header=0)
    if (trans_data["French_Name"].values != df_kbob["French_Name"].values).any():
        print('Warning: Some kbob terminology have changed : ')
        print(df_kbob.loc[~df_kbob["French_Name"].isin(trans_data["French_Name"].values), "French_Name"])
    if len(trans_data["French_Name"]) != len(df_kbob["French_Name"]):
        print('Error: Missing terminology in translation file')
        return
    df_kbob.index = trans_data["English_Name"]

    # save
    df_kbob.to_csv(name_base_csv + str(year) + ".csv")


def main():

    filename = "Liste Oekobilanzdaten im Baubereich 2009-1-2016-gerundet-kWh.xlsx"
    year = "2016"
    xls_to_csv(filename, year)


if __name__ == '__main__':
    main()