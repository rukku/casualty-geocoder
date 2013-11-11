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
            codelist[row[3]] = row[5]
    #print codelist
    print codelist
    for k,v in codelist.iteritems():
        print k,v

	writer = csv.writer(open("geocodes.csv", 'wb+'))    
	for k,v in codelist.iteritems():
		writer.writerow([k ,v]) 	

with open('dead.csv', 'rb') as f:
    reader = csv.reader(f)
    
    counts = defaultdict(int)
    
    for row in reader:
    	counts[row[3]] += 1

	for k,v in counts.iteritems():
	    print k,v   

	writer = csv.writer(open("deadcounts.csv", 'wb+'))    
	for k,v in counts.iteritems():
		gcode = str(checkgeocode(codelist[k]))
		writer.writerow([k ,v, gcode]) 	

    print counts
    json.dump(counts, open('dead.counts.json', 'w'))

with open('missing.csv', 'rb') as f:
    reader = csv.reader(f)
    
    counts = defaultdict(int)
    
    for row in reader:
    	counts[row[3]] += 1

	for k,v in counts.iteritems():
	    print k,v   

	writer = csv.writer(open("missingcounts.csv", 'wb+'))    
	for k,v in counts.iteritems():
		writer.writerow([k ,v,codelist[k]]) 	

    print counts
    json.dump(counts, open('dead.counts.json', 'w'))

with open('injured.csv', 'rb') as f:
    reader = csv.reader(f)
    
    counts = defaultdict(int)
    
    for row in reader:
    	counts[row[3]] += 1

	for k,v in counts.iteritems():
	    print k,v   

	writer = csv.writer(open("injuredcounts.csv", 'wb+'))    
	for k,v in counts.iteritems():
		writer.writerow([k ,v,codelist[k]]) 	

    print counts
    json.dump(counts, open('dead.counts.json', 'w'))
		#g = geocoders.GoogleV3()
		#place, (lat, lng) = g.geocode(row[3])  
		#print "%s: %.5f, %.5f" % (place, lat, lng)  