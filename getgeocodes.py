import csv

geocodes = dict()

with open('dead.csv', 'rb') as f:
    reader = csv.reader(f)
    
    codelist = dict()
    for row in reader:
            codelist[row[3]] = row[5]
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v
