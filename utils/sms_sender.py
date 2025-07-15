from twilio.rest import Client
import os
from dotenv import load_dotenv
from twilio.rest import Client
def send_sms(to_number: str, message: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number =os.getenv( "TWILIO_SMS_FROM")

    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(" SMS sent successfully.")
    except Exception as e:
        print(" Failed to send SMS:", e)
