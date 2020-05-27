import requests

def loadCanadaData():
    """Returns a csv file with data from Canada Covid 19 website """

    def loadArea(area):
        fileName = area + '.csv'
        areaData = open(fileName, 'w')

        with open("covidData.csv", 'r') as f:
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

    with open("covidData.csv",'wb') as f:
        f.write(r.content)

    for region in areas:
        loadArea(region)
#############   End of def loadCanada()
