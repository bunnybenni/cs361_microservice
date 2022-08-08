# name: Benni Taylor
# date: 8/8/2022
# class: CS 361
# description: Microservice Implementation
               # A microservice that takes an API key, a zip code/city, and a number of days up to 10 to retrieve data
               # for from .txt files, and then it retrieves the weather data from http://api.weatherapi.com/ and writes
               # the data to a weather_data.txt file that can be used by the user.

import json
import requests
import time

api_key_path = "api_key.txt"  # sign up at weatherapi.com for a free account to get an API key to put in the .txt file
zipcode_path = "zipcode.txt"  # zip codes and city/state queries both work here
days_out_path = "days_out.txt"  # data can be obtained up to 10 days out from the current date
write_txt_path = "weather_data.txt"

BASE_URL = "http://api.weatherapi.com/v1/forecast.json?"
API_KEY = open(api_key_path, 'r').read()


def get_weather():
    ZIPCODE = open(zipcode_path, 'r').read()
    DAYS_OUT = open(days_out_path, 'r').read()
    url = BASE_URL + "key=" + API_KEY + "&q=" + ZIPCODE + "&days=" + DAYS_OUT
    response = requests.get(url).json()
    with open(write_txt_path, 'w') as outfile:
        json.dump(response, outfile)
    print("weather data completed")

    # clear file data
    f = open(zipcode_path, 'w', encoding="utf-8")
    f.write(f"None")
    f.close()


if __name__ == "__main__":
    while True:
        # sleep for 1 second
        time.sleep(1)

        # open file zipcode_path and read
        f = open(zipcode_path, 'r', encoding="utf-8")
        line = f.readline()
        f.close()

        # if file is not empty:
        if line != "None":
            get_weather()
            print("Weather retrieved")


