

import csv

citylist = list()
count = 0
try:
    filename = "realestate.csv"
    with open(filename,"r") as fobj:
        for line in fobj.readlines()[0:16]:
            output = line.split(",")
            citylist.append(output[1])
        for city in set(citylist):
            print(city)
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
