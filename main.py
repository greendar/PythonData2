from dataMethods import *
import sys


areas = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba',
'Ontario', 'Quebec', 'Nova Scotia', 'New Brunswick', 'Newfoundland and Labrador',
'Prince Edward Island', 'Yukon', 'Nunavut', 'Northwest Territories', 'Canada']


loadCanadaData()

if len(sys.argv) > 1:
    choice = sys.argv[1]
else:
    choice = areaMenu(areas)

area = Region(choice + ".csv")

area.newCasesDate5DayAvg()
