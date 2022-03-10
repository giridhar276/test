
import csv

cityset = set()

try:
    filename = "realestate.csv"
    with open(filename,"r") as fobj:
        reader  = csv.reader(fobj)
        #processing
        for line in reader:
            city = line[1]
            cityset.add(city)
        #displaying
        for city in cityset:
            print(city)
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
