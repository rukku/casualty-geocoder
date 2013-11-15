#script that gets the geocodes
import csv

#build barangay codes
with open('alpha.geocodes.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()
	#build provincial codes    
    for row in reader:
            print row[7], row[6]
            codelist[row[7]] = int(float(row[6]))
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v, type(v)

	writer = csv.writer(open("geocodes.barangay.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k, v]) 	