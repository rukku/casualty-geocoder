#csv module.
import csv
from geopy import geocoders
from collections import defaultdict
import json

def checkgeocode(geocode):
	#return len(geocode)
	if len(geocode) < 9:
		return "0"+str(geocode)
	else:
		return geocode

with open('casualty.csv', 'rb') as f:
    reader = csv.reader(f)
    
    codelist = dict()
    for row in reader:
            codelist[row["Address"]] = row["AA_MUNCODE"]
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v

	writer = csv.writer(open("geocodes.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k ,v]) 	

