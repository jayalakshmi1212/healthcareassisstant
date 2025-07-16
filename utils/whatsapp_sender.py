
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_whatsapp_message(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_WHATSAPP_FROM")
    to_number = os.getenv("TWILIO_WHATSAPP_TO")

    client = Client(account_sid, auth_token)
    print("Sending SMS to:", to_number)

    
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    

    )

    return message.sid
