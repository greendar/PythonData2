import requests
import matplotlib.pyplot as plt
import pandas as pd

def loadCanadaData():
    """Returns a csv file with data from Canada Covid 19 website """

    def loadArea(area):
        fileName = 'Data/' + area + '.csv'
        areaData = open(fileName, 'w')

        with open("Data/covidData.csv", 'r') as f:
            for line in f:
                a = line.split(',')
                if a[1] == area:
                    tempList = [a[3], a[7], a[6]]
                    areaData.write(", ".join(tempList) + "\n")

    covidFile_url = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"

    areas = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba',
    'Ontario', 'Quebec', 'Nova Scotia', 'New Brunswick', 'Newfoundland and Labrador',
    'Prince Edward Island', 'Yukon', 'Nunavut', 'Northwest Territories', 'Canada']

    r = requests.get(covidFile_url) # create HTTP response object

    with open("Data/covidData.csv",'wb') as f:
        f.write(r.content)

    for region in areas:
        loadArea(region)


def revDate(dateIn):
    dateList = dateIn.split('-')
    dateList.reverse()
    return f"{dateList[0]}-{dateList[1]}-{dateList[2]}"

def averageThree(aList):
    bList = []
    for j in range(0, len(aList)):
        if j >= 2:
            bList.append(round((aList[j] + aList[j-1] + aList[j-2])/3, 2))
        else:
            bList.append(aList[j])
        j += 1
    return bList

def averageFive(aList):
    bList = []
    for j in range(0, len(aList)):
        if j >= 4:
            bList.append(round((aList[j] + aList[j-1] + aList[j-2] + aList[j-3] + aList[j-4])/5, 2))
        else:
            bList.append(aList[j])
        j += 1
    return bList

def averageSeven(aList):
    bList = []
    for j in range(0, len(aList)):
        if j >= 6:
            bList.append(round((aList[j] + aList[j-1] + aList[j-2] + aList[j-3] + aList[j-4] + aList[j-5] + aList[j-6])/6, 2))
        else:
            bList.append(aList[j])
        j += 1
    return bList

def areaMenu(listIn):
    i = 1
    for item in listIn:
        print(f"{i}. {item}")
        i += 1
    print('X. Exit')
    print()
    choice = input("Which would you like?  ")
    print()
    if choice == "X" or choice == "x":
        areaOut = 'Exit'
    else:
        areaOut = listIn[int(choice)-1]
    return areaOut


#############   End of def loadCanada()
class Region:
    def __init__(self, fName):
        self.fName = fName
        splitName = fName.split('.')
        self.name = splitName[0]
        self.totalCases = self.getTotalCases() # List
        self.newCases = self.diffListCases()
        self.totalDeaths = self.getTotalDeaths() # List
        self.newDeaths = self.diffListDeaths()
        self.dates = self.getDates()
        self.newCases3DayAvg = averageThree(self.newCases)
        self.newCases5DayAvg = averageFive(self.newCases)
        self.newCases7DayAvg = averageSeven(self.newCases)

    def getDates(self):
        dateList = []
        with open('Data/' + self.fName, 'r') as f:
            for line in f:
                a = line.split(', ')
                dateList.append(revDate(a[0]))
        return dateList

    def getTotalCases(self):
        totalCasesList = []
        with open('Data/' + self.fName, 'r') as f:
            for line in f:
                a = line.split(', ')
                totalCasesList.append(int(a[1]))
        return totalCasesList

    def getTotalDeaths(self):
        totalDeathsList = []
        with open('Data/' + self.fName, 'r') as f:
            for line in f:
                a = line.split(', ')
                totalDeathsList.append(int(a[2]))
        return totalDeathsList

    def diffListCases(self):
        previousTotal = 0
        a = []
        for item in self.totalCases:
            a.append(item - previousTotal)
            previousTotal = item
        return a

    def diffListDeaths(self):
        previousTotal = 0
        a = []
        for item in self.totalDeaths:
            a.append(item - previousTotal)
            previousTotal = item
        return a

    def graphScatter(self):
        plt.scatter(self.newCases, self.totalCases)
        plt.title(self.fName)
        plt.xlabel('New Cases')
        plt.ylabel('Total Cases')
        plt.show()


    def newCasesDate(self):
        date_time = self.dates
        date_time = pd.to_datetime(date_time)
        temp = self.newCases

        DF = pd.DataFrame()
        DF['temp'] = temp
        DF = DF.set_index(date_time)

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.3)
        plt.xticks(rotation=90)
        plt.plot(DF)
        plt.show()


    def newCasesDate3DayAvg(self):
        date_time = self.dates
        date_time = pd.to_datetime(date_time)
        temp = self.newCases3DayAvg

        DF = pd.DataFrame()
        DF['temp'] = temp
        DF = DF.set_index(date_time)

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.3)
        plt.xticks(rotation=90)
        plt.plot(DF)
        plt.show()


    def newCasesDate5DayAvg(self):
        date_time = self.dates
        date_time = pd.to_datetime(date_time)
        temp = self.newCases5DayAvg

        DF = pd.DataFrame()
        DF['temp'] = temp
        DF = DF.set_index(date_time)

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.3)
        plt.xticks(rotation=90)
        plt.title(f"{self.name} New Cases - 5 Day Average")
        plt.plot(DF)
        plt.grid()
        plt.show()

    def newCasesDate7DayAvg(self):
        date_time = self.dates
        date_time = pd.to_datetime(date_time)
        temp = self.newCases7DayAvg

        DF = pd.DataFrame()
        DF['temp'] = temp
        DF = DF.set_index(date_time)

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.3)
        plt.xticks(rotation=90)
        plt.title(f"{self.name} New Cases - 7 Day Average")
        plt.plot(DF)
        plt.grid()
        plt.show()
