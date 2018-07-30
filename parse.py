import csv
import json
MY_FILE="data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """parse function which parses a csv file and returns a json-like object"""
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
    return parsed_data

def main():
    new_data=parse(MY_FILE, ",")
    print (new_data)
    with open("outputfile", "w") as output:
        json.dump(new_data, output)

if __name__=="__main__":
    main()
