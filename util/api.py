import requests
import json
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("0x!b#(1*cd73w$&azzc6p+essg7v=g80ls#z&xcx*mpemx&@9$")


def getCovidData():
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
    'x-rapidapi-key': env("API_KEY"),
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers).json()
    return response