import csv

main_data = {}

file = open('Computers.csv')
reader = csv.reader(file)
for row in reader:
    if (row[0] != ""):
        value = dict()
        value['price'] = int(row[1])
        value['speed'] = int(row[2])
        value['hd']= int(row[3])
        value['ram'] = int(row[4])
        value['screen'] = int(row[5])
        value['cd'] = ("yes" == row[6])
        value['multi'] = ("yes" == row[7])
        value['premium'] = ("yes" == row[8])
        value['ads'] = int(row[9])
        value['trend'] = int(row[10])
        value['quality'] = value['speed']+value['hd']*2+value['ram']*10+value['screen']*3
        main_data[int(row[0])] = value
