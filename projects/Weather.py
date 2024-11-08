import sys
import requests
import json


# key:  a64eb441861ee904de3adf8ea947a821


def main():
    key = "a64eb441861ee904de3adf8ea947a821"
    while True:
        menu()
        try:
            userinput = int(input("What do you want to do? (1/2/3)\n"))
        except ValueError:
            continue
        match userinput:
            case 1:
                city = input("What city do you want?\n")
                countryname = input("What country is the city in?\n")
                prepare_geo_api_call(city, key)
            case 2:
                city = input("What city do you want?\n")
                countryname = input("What country is the city in?\n")
                response = prepare_geo_api_call(city, countryname, key)
                parse_geo_api_reponse(response)


def menu():
    print("------------------------------------------------------------------------")
    print("1. Get your location")
    print("2. Get the weather for your location (I still need your location then)")
    print("3. Quit")
    print("------------------------------------------------------------------------")


def prepare_geo_api_call(cityname, countrycode, apikey):
    reponse = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={cityname},{countrycode}&limit=5&appid={apikey}")
    finalresponse = reponse.json()
    return finalresponse


def prepare_weather_api_call(lat, lon, apikey):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={apikey}")
    finalresponse = response.json()
    return finalresponse


def parse_geo_api_reponse(response):
    data = json.loads(response)

    lat = data.get("lat")
    lon = data.get("lon")
    return {"lat": lat, "lon": lon}


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
