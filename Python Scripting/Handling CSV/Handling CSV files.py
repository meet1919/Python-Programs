import csv
examplefile = open('example.csv')
read = csv.reader(examplefile)
print(list(read))