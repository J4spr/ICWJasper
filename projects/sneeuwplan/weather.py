import requests


def get_weather_forecast(api_key, city="Leuven"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data["list"][:5]  # only first 5days

