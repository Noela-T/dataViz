# dataViz
A python console application that parses sample data from a public crime filings excel file(csv), from rows and columns to a list of dictionaries, then render that data in two different graphs with matplotlib and then as a map in GitHub using geoJSON.

#REQUIREMENTS

-python3
-install numpy
-install matplotlib

#WHAT WORKS

-Menu containing what the application can do.
-Parsing data from the csv file to get a list of dictionaries.
-Visualize_days function, which visualizes the data by the day of the week by plotting a graph of the frequency of incidents per day against the days of the week.
-Visualize_type function, which visualizes the data by the category/type of crime committed by plotting a bar chat of the frequency/rate for each type/category of crime.

#WHAT DOES NOT WORK

-Produce a geoJSON file for mapping

