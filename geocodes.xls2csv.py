import xlrd
import csv
import sys;

reload(sys);
sys.setdefaultencoding("utf8")

with xlrd.open_workbook('GeocodesVer2.xls') as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    with open('alpha.geocodes.csv', 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))