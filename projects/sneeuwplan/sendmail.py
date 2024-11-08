import base64
import os.path
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.compose"]


def authenticate_gmail():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


def create_draft(service, receiver_email, message):
    message_obj = EmailMessage()
    message_obj.set_content(message)
    message_obj["To"] = receiver_email
    message_obj["Subject"] = "Weerbericht"

    # Creating MIME message
    mime_message = MIMEMultipart()
    mime_message.attach(MIMEText(message))
    mime_message["To"] = receiver_email
    mime_message["Subject"] = "Weerbericht"

    # Encode and send
    encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
    create_message = {"message": {"raw": encoded_message}}

    draft = service.users().drafts().create(userId="me", body=create_message).execute()
    return draft


def main(mailadres, mail):
    try:
        service = authenticate_gmail()
        draft = create_draft(service, mailadres, mail)

        print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')
        service.users().drafts().send(userId="me", body=draft).execute()

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == '__main__':
    mailadres = input("Voer je e-mailadres in: ")
    mail = "Weersvoorspelling voor de komende vijf dagen in Leuven:\n\n"  # Add your weather details here
    main(mailadres, mail)
