'''
write a program to read realestate.csv and display each
city and the count of each city.
SACRAMENTO - 45 times
RIO LINDA   - 4 times
'''

import csv

#citylist = list()
#citylist = []

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
            print(city.ljust(20) , citylist.count(city),"times")

except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)

