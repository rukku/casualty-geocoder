#script that gets the geocodes
import csv

def checkgeocode(geocode):
    #return len(geocode)
    geocode = str(geocode)
    if len(geocode) < 9:
        return "0"+str(geocode)
    else:
        return geocode

writer = csv.writer(open("geocodes.citymun.cleaned.csv", 'wb+'))    
#build barangay codes
with open('geocodes.citymun.csv', 'rb') as f:
    reader = csv.reader(f)
    #next(reader, None) #skip header
    codelist = dict()
    #build provincial codes    
    for row in reader:
            #print row[7], row[6], type(row[6])
            #codelist[row[1]] = row[0]
            writer.writerow([row[1], checkgeocode(row[0])])   