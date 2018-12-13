#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import osem

setup(

    name='osef',

    version=osem.__version__,

    packages=find_packages(),

    author="CREM",

    author_email="osem@crem.ch",

    description="Open Source Energy Features: dedicated tools and methods for energy related models and applications",

    long_description=open('README.md').read(),

    # TODO: read from requirements.txt (or read/fill requirements.txt from steup.py ?)
    install_requires=["pandas"],

    include_package_data=True,

    url='',

    classifiers=[
        "Natural Language :: English",
        "Operating GraphCreator :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Topic :: Energy",
    ]

)