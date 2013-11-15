#script that gets the geocodes
import csv

def checkgeocode(geocode):
    #return len(geocode)
    geocode = str(geocode)
    if len(geocode) < 9:
        return "0"+str(geocode)
    else:
        return geocode

#build barangay codes
with open('alpha.geocodes.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()
	#build provincial codes    
    for row in reader:
            #print row[7], row[6], type(row[6])
            codelist[row[3]] = int(float(row[2]))

    writer = csv.writer(open("geocodes.province.csv", 'wb+'))    
    for k,v in codelist.iteritems():
        print k,v, type(v) 
        writer.writerow([k, checkgeocode(v)]) 	