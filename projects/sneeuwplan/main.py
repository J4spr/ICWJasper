import base64
import os.path
from email.message import EmailMessage

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv_vault import load_dotenv

load_dotenv()
token = os.getenv("WEATHER_TOKEN")
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.compose"]


def get_weather_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data["list"][:5]  # only first 5days


def main():
    google_credentials_file = "credentials.json"

    # Fetching weather forecast
    city = input("Enter city")
    weather_forecast = get_weather_forecast(token, city)

    message = f"Weersvoorspelling voor de komende vijf dagen in {city}:\n\n"
    for forecast in weather_forecast:
        date = forecast["dt_txt"].split()[0]
        temperature = forecast["main"]["temp"]
        description = forecast["weather"][0]["description"]
        wind_speed = forecast["wind"]["speed"]
        precipitation = forecast["rain"]["3h"] if "rain" in forecast else 0

        message += f"Datum: {date}\n"
        message += f"Temperatuur: {temperature} °C\n"
        message += f"Neerslag: {precipitation} mm\n"
        message += f"Weer: {description}\n"
        message += f"Windsnelheid: {wind_speed} m/s\n\n"

    # Sending email
    mailadres = input("Voer je e-mailadres in: ")
    mail = message
    send_email(google_credentials_file, mailadres, mail)


def send_email(credentials_file, receiver_email, message):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as tokenfile:
            tokenfile.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)

        message_obj = EmailMessage()
        message_obj.set_content(message)
        message_obj["To"] = receiver_email
        message_obj["Subject"] = "Weerbericht"

        encoded_message = base64.urlsafe_b64encode(message_obj.as_bytes()).decode()

        create_message = {"message": {"raw": encoded_message}}

        draft = (
            service.users()
            .drafts()
            .create(userId="me", body=create_message)
            .execute()
        )
        print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')
        service.users().drafts().send(userId="me", body=draft).execute()

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == '__main__':
    main()
