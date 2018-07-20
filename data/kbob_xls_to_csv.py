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
    filename_unit = "kbob_unit{}.json".format(year)

    # Load raw-excel
    df_kbob = pd.read_excel(filename, sheet_name=sheetname, skiprows=6, usecols=[4, 5, 6, 7, 8, 9, 11])

    # rename columns
    with open(filename_unit, 'r') as fp:
        col_unit = json.load(fp)

    df_kbob.rename(columns={k: v for k, v in zip(df_kbob.columns, col_unit.keys())}, inplace=True)

    df_kbob["FRA"] = df_kbob["FRA"].str.replace(',', ' -')
    df_kbob.dropna(inplace=True)

    # add language
    trans_data = pd.read_csv(filename_trans, header=0)
    df_kbob = pd.merge(df_kbob, trans_data, on="FRA")

    # export
    df_kbob.to_csv("{}{}.csv".format(name_base_csv, year))


def main():

    filename = "Liste Oekobilanzdaten im Baubereich 2009-1-2016-gerundet-kWh.xlsx"
    year = "2016"
    xls_to_csv(filename, year)


if __name__ == '__main__':
    main()
