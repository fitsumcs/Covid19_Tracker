from django.shortcuts import render
import requests
import json
from util.api import getCovidData, getContex


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
        context = getContex(countryList,selectedCountry,noCountries)
        return render(request,'hello.html',context)

    context = {'countryList': countryList}
    return render(request,'hello.html',context)
