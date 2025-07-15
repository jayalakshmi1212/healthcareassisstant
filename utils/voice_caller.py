import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_VOICE_FROM")
TWILIO_TO = os.getenv("TWILIO_VOICE_TO")  # for testing only

client = Client(TWILIO_SID, TWILIO_AUTH)

def make_voice_call():
    call = client.calls.create(
        url="https://handler.twilio.com/twiml/EHd5b43990e7185ac4df2210f121cecc5d",  # Replace <your-ip> if needed
        to=TWILIO_TO,
        from_=TWILIO_FROM
    )
    return call.sid