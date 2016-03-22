import csv
import main

main_data = {}

file = open('Computers.csv')
reader = csv.reader(file)
for row in reader:
    if (row[0] != ""):
        value = dict()
        value['price'] = int(row[1])
        value['speed'] = int(row[2])
        main_data[int(row[0])] = value
