
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(filename: str) -> str:
    with open(filename, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
    return transcript.text

def transcribe_audio_from_url(audio_url: str):
    from requests.auth import HTTPBasicAuth

    twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_token = os.getenv("TWILIO_AUTH_TOKEN")

    download_url = audio_url 

    response = requests.get(download_url, auth=HTTPBasicAuth(twilio_sid, twilio_token))

    if response.status_code != 200:
        raise Exception("Failed to download Twilio audio file")

    with open("temp_audio.mp3", "wb") as f:
        f.write(response.content)

    with open("temp_audio.mp3", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
    return transcript.text

