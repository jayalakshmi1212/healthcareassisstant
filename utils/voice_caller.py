from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SMS_FROM = os.getenv("TWILIO_SMS_FROM")  # e.g., +16293069996
TO_PHONE_NUMBER = os.getenv("TWILIO_VOICE_TO")  # e.g., your verified number like +91xxxxxxxxxx

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def make_voice_call():
    call = client.calls.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_SMS_FROM,
        url="https://handler.twilio.com/twiml/EHbcf4f28062c225ebe25f2ede3d7a8326"  
    )
    print(f"✅ Voice call initiated. SID: {call.sid}")
