from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "64bca0886bmsha7377930000aed5p1a6aecjsn8fa7b68dbbfb",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloWorld(request):
    noCountries = response['results']
    if request.method == "POST":
        selectedCountry = request.POST['countries']
        print(selectedCountry)
        for i in range(0,noCountries):
            if selectedCountry == response['response'][i]['country']:
                newCases = response['response'][i]['cases']['new']
                activeCases = response['response'][i]['cases']['active']
                criticalCases = response['response'][i]['cases']['critical']
                recoveredCases = response['response'][i]['cases']['recovered']
                totalCases = response['response'][i]['cases']['total']
                deathCases = totalCases - activeCases - recoveredCases
                print(deathCases)
        context = {'newCases': newCases,'activeCases': activeCases,'criticalCases': criticalCases,'recoveredCases': recoveredCases,'totalCases': totalCases,'deathCases': deathCases}
   
    countryList = []
    for i in range(0,noCountries):
        countryList.append(response['response'][i]['country'])
    context = {'countryList': countryList}
    return render(request,'hello.html',context)
