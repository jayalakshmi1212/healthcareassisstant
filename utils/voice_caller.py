import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

def make_voice_call():
    call = client.calls.create(
        url="https://healthcare-assistantt.onrender.com/twiml",
        to=os.getenv("TWILIO_VOICE_TO"),
        from_=os.getenv("TWILIO_VOICE_FROM")
    )
    return call.sid
