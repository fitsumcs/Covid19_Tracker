from django.shortcuts import render
import requests
import json
from util.api import getCovidData, getContex , getCountryList


# Get Covid Data 
response = getCovidData()

# Create your views here.
def covidDisplay(request):
    noCountries = response['results']
    countryList = getCountryList(noCountries)
    countryList = sorted(countryList)
    
    if request.method == "POST":
        selectedCountry = request.POST['countries']
        context = getContex(countryList,selectedCountry,noCountries)
        return render(request,'hello.html',context)

    context = {'countryList': countryList}
    return render(request,'hello.html',context)
