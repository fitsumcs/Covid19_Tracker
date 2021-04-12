from django.shortcuts import render
import requests
import json
from util.api import getCovidData


# Get Covid Data 
response = getCovidData()

# Create your views here.
def covidDisplay(request):
    noCountries = response['results']
    countryList = []
    for i in range(0,noCountries):
        countryList.append(response['response'][i]['country'])
    if request.method == "POST":
        selectedCountry = request.POST['countries']
        for i in range(0,noCountries):
            if selectedCountry == response['response'][i]['country']:
                newCases = response['response'][i]['cases']['new']
                activeCases = response['response'][i]['cases']['active']
                criticalCases = response['response'][i]['cases']['critical']
                recoveredCases = response['response'][i]['cases']['recovered']
                totalCases = response['response'][i]['cases']['total']
                deathCases = totalCases - activeCases - recoveredCases
        context = {'selectedCountry' : selectedCountry,'countryList': countryList,'newCases': newCases,'activeCases': activeCases,'criticalCases': criticalCases,'recoveredCases': recoveredCases,'totalCases': totalCases,'deathCases': deathCases}
        return render(request,'hello.html',context)

    context = {'countryList': countryList}
    return render(request,'hello.html',context)
