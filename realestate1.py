#write a program to read realestate.csv and display
#street and city columns only with proper exception handling



import csv

try:
    filename = "realestate.csv"
    with open(filename,"r") as fobj:
        reader  = csv.reader(fobj)
        for line in reader:
            print("Street:", line[0])
            print("City  :", line[1])
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
