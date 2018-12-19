.. osem documentation master file, created by
   sphinx-quickstart on Mon Nov 19 09:00:43 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   
.. toctree::
   :maxdepth: 3
   :caption: Contents:

Welcome to OSEM's documentation!
================================
Open Source Energy Module: dedicated tools and methods for energy related models and applications

Presentation
*********************************************

The OSEM module collects different functions which are useful to energy planners. The functions contained in this module can be grouped in 
four types:

* Functions to accesss usual data: This part is centered on the Swiss energy market and contain API to access databases about price, C02 emissions and primary energy usage of various heating technology (also known as kbob). It also includes tools to access meteorological data from Switzerland. 
* Functions to estimate energy demands from buildings.
* Models of different energy technology (production, distribution, storage, and conversion), including functions to simulate natural gas network.
* Plotting functions for different energy indicators (primary energy, useful energy, etc.).

OSEM is currently under developement and is expected to be ready for production in 2019. It is an evolution of the EnerAPI module and many functions from EnerAPI are part of the OSEM module.


Getting Started
==================================================

To install OSEM, clone the repository and run the set-up: 

* git clone https://gitlab.com/crem-repository/OSEF.git
* sudo python setup.py install

You can test this module using Pytest (https://docs.pytest.org/en/latest/)

Access Data
===================================================
This sub-module contains the different functions to reach and manage usual datasets related to energy. It contains data about C02 emission, final energy, and Swiss price. Usual political objectives in term of energy policy is also included.

Kbob data
*******************************
This module contains usual values for different energy parameters such as CO2 emission, final energy for different technologies (Kbob). More information on the Kbob here : https://www.kbob.admin.ch/kbob/fr/home/publikationen/nachhaltiges-bauen/oekobilanzdaten_baubereich.html


.. automodule:: osem.access_data.kbob
	:members:

	
KPI computation
**************************************
This sub-module is based on the kbob module and it computes usual energy parameters (Co2 emission, primary energy, etc.) for different heating technologies. These functions take the primary energy consumed by different technologies for different years and/or scenarios as input.

.. automodule:: osem.access_data.kpi
	:members:

	
Meteorological Data
*****************************************
This sub-module contains basic meteorological data from the main swiss meterological station. It also contains a function which finds the closest station from a particular point.

.. automodule:: osem.access_data.meteo
	:members:

Price
******************************************
This sub-module contains a database with CAPEX/OPEX for the Swiss market. These price are taken from various sources which are listed in the database.

.. automodule:: osem.access_data.price
	:members:
	
Political Objectives
******************************************
This sub-module contains a list of different political objective for the swiss governement.

.. automodule:: osem.access_data.political_objective
	:members:
	
Energy Production & Transformation
===========================================
This sub-module regroups tools to simulate different technology to transform energy.

Heat Pump
********************************************
This module transforms 
 .. automodule:: osem.models.heatpump
	:members:

	
Gas Network (pandangas).
============================================
This sub-module allows to simulate a gas network using an API similar to pandaspower for electricity network.

Network creation
*******************************************
This group of functions contains the tools to create a new natural gas network.

.. automodule:: osem.networks.pandangas.network_creation
	:members:
	:special-members:
	:private-members:

Simulation
******************************************
These functions are used to run a new simulation of natural gas network.
	
.. automodule:: osem.networks.pandangas.run_simulation
	:members:
	:special-members:
	:private-members:

	
Utilities
******************************************
This is a group of function which are useful to manipulate data related natural gas network.

.. automodule:: osem.networks.pandangas.utilities
	:members:
	:special-members:
	:private-members:

	
	
Plot
=====================================================
This sub-module is composed of funtions to create different plots easily.

.. automodule:: osem.plot.plot_kpi
	:members:

General
===================================================
This sub-module contains the configuration options for OSEM and functions which are common to different OSEM models.

.. automodule:: osem.general.conf
	:members:

	
.. automodule:: osem.general.helper
	:members:


Authors 
==============================================

* Lesly Houndole
* Pablo Puerto
* Jakob Rager
* Diane von Gunten

(by alphabetical order)

License
=========================================================

You should have received a copy of the Apache License Version 2.0 along with this program.
If not, see http://www.apache.org/licenses/LICENSE-2.0.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
