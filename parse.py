from collections import Counter
import csv
import json
import matplotlib.pyplot as plt
import numpy as np

MY_FILE="data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """parse function which parses a csv file and returns a json-like object
       which represents the parsed data without its column headers and a list
       object fields which is the list of column headers"""
    #open CSV file
    opened_file  = open(raw_file)
    #read CSV file
    csv_data=csv.reader(opened_file, delimiter=delimiter)
    #close CSV file
    #build a data structure to return parsed_data
    parsed_data=[]
    #skip over the first line of the file for the headers
    fields=csv_data.__next__()
    #Iterate over each row of the csv file, zip together field->Value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    #close the csv file
    opened_file.close()
    return parsed_data,fields

def visualize_days():
    """Visualize data by the day of the week"""
    #parsed data that we parsed earlier
    data_file=parse(MY_FILE, ",")[0]
    #make a new variable, 'counter' from iterating through each line of data in
    #the parsed data, and count how many incidents happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)
    #separate the y-axis data (the number of incidents for each day)
    data_list=[counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]
    # from the x-axis data (days of the week). Using a tuple because the matplotlib
    #only accepts tuples for labeling the x-axis
    data_tuple=tuple(["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
    #with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    #create the amount of ticks needed for our x-axis, and assign the labels
    plt.xticks(range(len(data_tuple)), data_tuple)
    #save the plot
    plt.show()
    #plt.savefig("Days.png")
    #close plot file
    plt.clf

def displayData():
    """Prints out the raw data in the csv file"""
    data, fields=parse(MY_FILE, ",")
    #prints each row(crime) in the csv_file including the column headers
    for row in data:
        for field in fields:
            print (field + ":", end="")
            print(row[field]+".", end=" ")
        print("\n")
