# dataViz
A python console application that parses sample data from a public crime filings excel file(csv), from rows and columns to a list of dictionaries, then render that data in two different graphs with matplotlib and then as a map in GitHub using geoJSON.

## REQUIREMENTS

```
- python3
- install numpy
- install matplotlib
- install geojson
```
## RUN PROGRAM
1. In your terminal, go to the directory containing this repository.
   
2. Type ```python3 main.py``` to launch the program.

## WHAT WORKS
- Menu containing what the application can do.
- Parsing data from the csv file to get a list of dictionaries.
- Visualize_days function, which visualizes the data by the day of the week by plotting a graph of the frequency of incidents per day against the days of the week.
- Visualize_type function, which visualizes the data by the category/type of crime committed by plotting a bar chat of the frequency/rate for each type/category of crime.
- Produce a geoJSON file for mapping

## TROUBLESHOOTING
 
If you have problems with installing any of the required libraries, I suggest you use virtualenv (an isolated working copy of Python which allows you to work on a specific project without worry of affecting other projects), more on virtualenv [here](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv).
1. To install virtualenv, in your terminal type ```pip3 install virtualenv```
2. To create a new virtual environment for the project, navigate to the project directory and run the command 
    ```python3 -m venv myvenv``` where myvenv is the name of the virtual environment you want to create.
3. To activate your virtual environment
    ```source myvenv/bin/activate```
Now, you can then install the libraries listed above and be sure of no conflict problems.
Make sure to run the program as stated above in the virtual environment you created.
When you are done with the program, you can exit the virtual environment by running the command 
  ```deactivate```


