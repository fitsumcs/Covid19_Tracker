import requests
import json
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()


SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")


def getCovidData():
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
    'x-rapidapi-key': env('API_KEY'),
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers).json()
    return response