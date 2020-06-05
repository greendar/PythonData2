from dataMethods import *


areas = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba',
'Ontario', 'Quebec', 'Nova Scotia', 'New Brunswick', 'Newfoundland and Labrador',
'Prince Edward Island', 'Yukon', 'Nunavut', 'Northwest Territories', 'Canada']


loadCanadaData()

choice = areaMenu(areas)

area = Region(choice + ".csv")

area.newCasesDate5DayAvg()
