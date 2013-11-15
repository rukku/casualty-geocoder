from mmap import mmap,ACCESS_READ
from xlrd import open_workbook

print open_workbook('GeocodesVer2.xls')
with open('GeocodesVer2.xls','rb') as f:
	print open_workbook(
 	file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
 	)

aString = open('GeocodesVer2.xls','rb').read()
print open_workbook(file_contents=aString)