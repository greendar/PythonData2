from dataMethods import *
from graphing import *

loadCanadaData()

area = Region("Ontario.csv")

a = list(range(1, len(area.totalCases)+1))

print(a)

graphPlot(a, area.totalCases)
