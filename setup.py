#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import osem

setup(

    name='osem',

    version=osem.__version__,

    packages=find_packages(),

    author="CREM",

    author_email="osem@crem.ch",

    description="Open Source Energy Features: dedicated tools and methods for energy related models and applications",

    long_description=open('README.md').read(),

    # TODO: read from requirements.txt (or read/fill requirements.txt from steup.py ?)
    install_requires=["pandas","scipy","thermo","networkx","numpy","thermo","xlrd","fluid","mpmath","sympy"],

    include_package_data=True,

    url='https://www.crem.ch/',

    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],

    data_files = [('', ['osem/general/data/kpi_efficiency_heating.csv',
                        'osem/general/data/kpi_example_2.xlsx',
                        'osem/general/data/kpi_example_c02.xlsx',
                        'osem/general/data/pandangas_info_solver_option.json',
                        'osem/general/data/political_obj.csv',
                        'osem/general/data/price_create_database.py',
                        'osem/general/data/price_database.db',

                        'osem/general/data/data_kbob/kbob_data2016.csv',
                        'osem/general/data/data_kbob/kbob_data2222.csv',
                        'osem/general/data/data_kbob/kbob_translation_indicator.csv',
                        'osem/general/data/data_kbob/kbob_translation_tech.csv',
                        'osem/general/data/data_kbob/kbob_unit2016.json',
                        'osem/general/data/data_kbob/kbob_unit2222.json',
                        'osem/general/data/data_kbob/kbob_xls_to_csv.py',
                        'osem/general/data/data_kbob/Liste Oekobilanzdaten im Baubereich 2009-1-2016-gerundet-kWh.xlsx',


                        'osem/general/data/data_meteo_swiss/atmospheric_pressure.txt',
                        'osem/general/data/data_meteo_swiss/data_source.txt',
                        'osem/general/data/data_meteo_swiss/global_radiation.txt',
                        'osem/general/data/data_meteo_swiss/nb_day_precipitation.txt',
                        'osem/general/data/data_meteo_swiss/nb_hour_solar_rad.txt',
                        'osem/general/data/data_meteo_swiss/precipitations.txt',
                        'osem/general/data/data_meteo_swiss/relative_humidity.txt',
                        'osem/general/data/data_meteo_swiss/temperature_max.txt',
                        'osem/general/data/data_meteo_swiss/temperature_mean.txt',
                        'osem/general/data/data_meteo_swiss/temperature_min.txt',

                        'osem/general/data/enerapi_data/affect_RegBL.json',
                        'osem/general/data/enerapi_data/boiler_techno.json',
                        'osem/general/data/enerapi_data/Construct_Bat.json',
                        'osem/general/data/enerapi_data/Data_Project_Nature.json',
                        'osem/general/data/enerapi_data/Data_Qhli.json',
                        'osem/general/data/enerapi_data/data_SIA_380-1.json',
                        'osem/general/data/enerapi_data/em_system.json',
                        'osem/general/data/enerapi_data/Meteo2028.json',
                        'osem/general/data/enerapi_data/period_RegBL.json',
                        'osem/general/data/enerapi_data/ratio_base.json',
                        'osem/general/data/enerapi_data/SSE_Coef_Orient.json',
                        'osem/general/data/enerapi_data/WindowRatio.json',
                        'osem/general/data/enerapi_data/WindowTypeIncidentRate.json',])],


)