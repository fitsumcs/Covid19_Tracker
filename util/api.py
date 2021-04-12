import requests
import json
import environ

env = environ.Env()

def getCovidData():
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
    'x-rapidapi-key': env('API_KEY'),
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers).json()
    return response

# Get Context 
def getContex(countryList,selectedCountry,noCountries):
    response = getCovidData()
    for i in range(0,noCountries):
        if selectedCountry == response['response'][i]['country']:
            newCases = response['response'][i]['cases']['new']
            activeCases = response['response'][i]['cases']['active']
            criticalCases = response['response'][i]['cases']['critical']
            recoveredCases = response['response'][i]['cases']['recovered']
            totalCases = response['response'][i]['cases']['total']
            deathCases = totalCases - activeCases - recoveredCases
            context = {'selectedCountry' : selectedCountry,'countryList': countryList,'newCases': newCases,'activeCases': activeCases,'criticalCases': criticalCases,'recoveredCases': recoveredCases,'totalCases': totalCases,'deathCases': deathCases}
            return context