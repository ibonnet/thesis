# Datasets

## Overview
This folder contains all the datasets used for my Master's thesis, which tracked all flight routes to Venezuela since 2020. The datasets were primarily sourced from <b>FlightRadar24</b>, and were used to create maps using <b>QGIS</b>. In addition to the flight data, this folder also contains datasets related to tourism to Venezuela.

## Datasets
### Files
<li><b>Airport_CRS_Coordinates.csv:</b> All commercial flights arriving to Venezuela between 2020 and 2023. The data is based on all scheduled non-stop flights to Venezuela during a 7-day period as of April 6, 2023, and has been sourced from FlightRadar24.</li>
<li><b>Flights_Venezuela_2020_2023.csv:</b> Airport data, which includes IATA codes, ISO codes, airport names, latitude and longitude coordinates, and corresponding CRS easting and northing values. This data can be used for various geographic and aviation-related analyses and visualizations.</li>

### Keywords
<li><b>CRS:</b> CRS stands for <a href="https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/coordinate_reference_systems.html">Coordinate Reference System</a>, which refers to a specific way of representing geographic coordinates. The coordinates are in decimal degrees, which is a commonly used format for geographic coordinates.</li>
<li><b>IATA:</b> IATA stands for the <a href="https://www.iata.org/en/youandiata/airports/">International Air Transport Association</a>, which is a trade association of the world's airlines. The IATA assigns a unique two-letter code, known as the IATA code, to identify airports and airlines around the world.</li>
<li><b>ISO:</b> The ISO country codes are a standard set of two-letter codes assigned to countries and territories by the <a href="https://www.iso.org/members.html">International Organization for Standardization (ISO)</a>.</li>

## Maps
The maps in this folder were created using QGIS and the flight data from <b>Flights_Venezuela_2020_2023.csv</b>. The maps visualize the flight routes to Venezuela from different regions of the world.

## Usage
The datasets in this folder can be used for further analysis or visualization of flight routes and tourism to Venezuela. The maps can be used to gain a better understanding of the connectivity between Venezuela and other regions of the world.

## Credits
<li><a href="https://www.flightradar24.com/data/airports/venezuela">FlightRadar24:</a> primary source for flight data.</li>
<li><a href="https://qgis.org/en/site/">QGIS:</a> software used to create the flight route maps.</li>
