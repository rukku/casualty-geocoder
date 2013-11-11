#script that gets the geocodes
import csv


with open('alpha.geocodes.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()

	#build regional codes    
    for row in reader:
            codelist[row[1]] = int(float(row[0]))
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v, type(v)

	writer = csv.writer(open("geocodes.region.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k, v]) 

with open('alpha.geocodes.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()
	#build provincial codes    
    for row in reader:
            codelist[row[3]] = int(float(row[2]))
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v, type(v)

	writer = csv.writer(open("geocodes.province.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k, v]) 

#build city codes
with open('alpha.geocodes.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()
	#build provincial codes    
    for row in reader:
            codelist[row[5]] = int(float(row[4]))
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v, type(v)

	writer = csv.writer(open("geocodes.citymun.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k, v]) 	

#build barangay codes
with open('alpha.geocodes.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()
	#build provincial codes    
    for row in reader:
            codelist[row[7]] = int(float(row[6]))
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v, type(v)

	writer = csv.writer(open("geocodes.barangay.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k, v]) 	