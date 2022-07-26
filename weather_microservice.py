# name: Benni Taylor
# date: 7/25/2022
# class: CS 361
# description: Microservice Implementation
import json

import requests

api_key_path = "api_key.txt"
zipcode_path = "zipcode.txt"
days_out_path = "days_out.txt"
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
