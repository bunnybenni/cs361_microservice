# name: Benni Taylor
# date: 7/25/2022
# class: CS 361
# description: Microservice Implementation
               # A microservice that takes an API key, a zip code/city, and a number of days up to 10 to retrieve data
               # for from .txt files, and then it retrieves the weather data from http://api.weatherapi.com/ and writes
               # the data to a weather_data.txt file that can be used by the user.

import json
import requests

api_key_path = "api_key.txt"  # sign up at weatherapi.com for a free account to get an API key to put in the .txt file
zipcode_path = "zipcode.txt"  # zip codes and city/state queries both work here
days_out_path = "days_out.txt"  # data can be obtained up to 10 days out from the current date
write_txt_path = "weather_data.txt"

BASE_URL = "http://api.weatherapi.com/v1/forecast.json?"
API_KEY = open(api_key_path, 'r').read()
ZIPCODE = open(zipcode_path, 'r').read()
DAYS_OUT = open(days_out_path, 'r').read()


def get_weather():
    url = BASE_URL + "key=" + API_KEY + "&q=" + ZIPCODE + "&days=" + DAYS_OUT
    response = requests.get(url).json()
    with open(write_txt_path, 'w') as outfile:
        json.dump(response, outfile)


def main():
    get_weather()


if __name__ == "__main__":
    main()
