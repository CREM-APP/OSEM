# OSEM
Open Source Energy Module: dedicated tools and methods for energy related models and applications


## Presentation

The OSEM module collects different functions which are useful to energy planners. The functions contain in this module can be grouped in 
four types:

* Functions to accesss usual data: This part is centered on the Swiss energy market and contain API to access databases about price, C02 
emissions and primary energy usage of various heating technology (also known as kbob). A database about the norm SIA 308/1 
and different swiss political objectives will also be developed.
* Functions to estimate energy demands from buildings.
* Models of different energy technology (production, distribution, storage, and conversion).
* Functions to support GIS-based creation of gas/electricity-network.
* Plotting functions for different energy indicators (primary energy, useful energy, etc.).

OSEM is currently under developement and is expected to be ready for production in 2019.


## Getting Started

To install OSEM, clone the repository and run the set-up: 

$ git clone https://gitlab.com/crem-repository/OSEF.git
$ sudo python setup.py install

You test this module using Pytest (https://docs.pytest.org/en/latest/)


## Authors 

* Albain Dufils
* Lesly Houndole
* Pablo Puerto
* Jakob Rager
* Diane von Gunten

(by alphabetical order)

## License

You should have received a copy of the Apache License Version 2.0 along with this program.
If not, see http://www.apache.org/licenses/LICENSE-2.0.

