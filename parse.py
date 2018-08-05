from collections import Counter
import csv
import json
import sys
import webbrowser
import matplotlib.pyplot as plt
import numpy as np
import geojson

MY_FILE="data/sample_sfpd_incident_all.csv"

def menu():
    """Displays a menu which shows what can be done with the program"""
    while True:
        print("""
           MENU
           1.Display raw data from file
           2.Visualize data by the day of the week
           3.Visualize data by the category of the crime in a bar graph
           4.Create a GeoJSON file to visualize the data on a map that can be
           rendered on Github Gist at gist.github.com
           5.exit program
           """)
        option=input("Enter your choice: ")
        if option == '1':
            displayData()
        elif option == '2':
            visualize_days()
        elif option == '3':
            visualize_type()
        elif option == '4':
            create_map(parse(MY_FILE,",")[0])
            print("""
                Your GeoJSON file has been created.To view the map directly on
                GitHub Gist, enter yes. If you prefer to create yout own Gist,
                 enter no.\n""")
            test=True
            while test == True:
                option2=input("Enter your choice: ")
                if ('y' in option2):
                    webbrowser.open("https://gist.github.com/Noela-T/fc95866ac4bca770677f4fe342985ac4#file-data-geojson")
                    test = False
                elif ('n' in option2):
                    print("""
                        To create your own Gist;
                        1.Navigate to gist.github.com.
                        2.Then copy the text in the newly-created geojson file,
                         and paste into the Gist.
                        3.Make sure to name your gist file with the .geojson
                        ending
                        4.Then select either “Create Private Gist” or
                        “Create Public Gist”, your choice
                        ....And Voila!!...""")
                    test=False
                else:
                    print("Please enter an appropriate answer.")
                    test=True
        elif option == '5':
            sys.exit()
        else:
            print('\n***Enter the appropriate number.***\n')

def parse(raw_file, delimiter):
    """parse function which parses a csv file and returns a json-like object
       which represents the parsed data without its column headers and a list
       object fields which is the list of column headers"""
    #open CSV file
    opened_file  = open(raw_file)
    #read CSV file
    csv_data=csv.reader(opened_file, delimiter=delimiter)
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
    """Visualize data by the day of the week. That is by plotting a graph of
        frequency of incidents per day(y-axis) against the days of the week(x-axis)"""
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
    #displays plot file
    plt.show(block=False)
    #save the plot
    #plt.savefig("Days.png")

def visualize_type():
    """Vizualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")[0]
    #grabing incidents that happen by category
    counter = Counter(item["Category"] for item in data_file)
    #set labels which are based on the keys of our counter
    labels=tuple(counter.keys())
    #set where the labels hit the x-axis
    xlocations=np.array(range(len(labels))) + 0.5
    #width of each bar
    width=0.5
    #Assign data to a bar plot, with the counter values being the heights of the bars
    plt.bar(xlocations, counter.values(), width=width)
    #Assign labels and tick location to x-axis
    #width/2, place bar at the center of the tick
    plt.xticks(xlocations + width/2, labels, rotation=90)
    #Give some more room so the labels aren't cut off from the graph
    plt.subplots_adjust(bottom=0.4)
    #make an overall graph/figure larger
    plt.rcParams['figure.figsize']=12, 8
    plt.savefig("Type.png")
    plt.show(block=False)
    #plt.clf()

def displayData():
    """Prints out the raw data in the csv file"""
    data, fields=parse(MY_FILE, ",")
    #prints each row(crime) in the csv_file including the column headers
    for row in data:
        for field in fields:
            print (field + ":", end="")
            print(row[field]+".", end=" ")
        print("\n")

def create_map(data_file):
    """Creates a GeoJSON file.
    Returns a GeoJSON file that can be rendered in a GitHub Gist at gist.github.com.
    Just copy the output file and paste into a new Gist, then create either a
    public or private gist. Github will automatically render the GeoJSON file as a map.
    """
    #define type of GeoJSON we're creating
    geo_map={"type":"FeatureCollection"}
    #define empty list to collect each point to graph
    item_list=[]
    #iterate over data to create GeoJSON document
    #enumerate(), so we get the line, as well as the line number(index)
    for index, line in enumerate(data_file):
        #skip any zero coordinates as this will throw off the map
        if line['X']=="0" or line['Y']=="0":
            continue
        #setup a new dictionary for each iteration
        data={}
        #assign line items to appropriate GeoJSON fields
        data['type']='Feature'
        data['id']=index
        data['geometry']={'type':'Point',
                          'coordinates':(line['X'],line['Y'])}
        data['properties']={'title':line['Category'],
                            'description':line['Descript'],
                            'date':line['Date']}
        #adding data dictionary to item_list
        item_list.append(data)
    #for each item on our item_list, we add it to our geomap dictionary
    #setdefault creates a key called 'features' that has a value type of an empty listt
    #with each iteration, we are appending the item to item_list
    for item in item_list:
        geo_map.setdefault('features', []).append(item)
    #save the parsed GeoJson data to a file so it can be uploaded to
    #gist.github.com
    with open('file_sf.geojson','w')as f:
        f.write(geojson.dumps(geo_map))
