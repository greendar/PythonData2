from dataMethods import *
import sys


areas = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba',
'Ontario', 'Quebec', 'Nova Scotia', 'New Brunswick', 'Newfoundland and Labrador',
'Prince Edward Island', 'Yukon', 'Nunavut', 'Northwest Territories', 'Canada']

#########################################
'''
Next make it so that if a command line choice
is not in areas then will default to internal
menu
'''
#########################################

loadCanadaData()

if len(sys.argv) > 1: # can use command line
    choice = sys.argv[1]
else: # or the internal menu
    choice = areaMenu(areas)

area = Region(choice + ".csv")

area.newCasesDate7DayAvg()
