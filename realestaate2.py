#write a program to read realestate.csv and
#display all the unique cities and also display total no. of cities

import csv

citylist = list()

try:
    filename = "realestate.csv"
    with open(filename,"r") as fobj:
        reader  = csv.reader(fobj)
        #processing
        for line in reader:
            city = line[1]
            citylist.append(city)
        #displaying
        for city in set(citylist):
            print(city)
    print()
    print()
    print("Total no. of cities :", len(set(citylist)))
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)

