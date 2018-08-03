import parse

def main():
    print("""
            **********DATA VISUALIZATION PROGRAM**********\n
            This program can takes data from csv files,parses the data from
            rows and columns to list of dictionaries and then renders the data
            in different graphs as shown on the menu.
        """)
    parse.menu()

if __name__=="__main__":
    main()
