import csv;

SourceFile="C:\\Work\\Andromeda\\Primus SIT & CC\\20180103\\Book1.csv";


with open(SourceFile, 'rb') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print ', '.join(row)
