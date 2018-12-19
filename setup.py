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
    ]

)