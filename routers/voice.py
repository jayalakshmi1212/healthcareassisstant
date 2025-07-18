from fastapi import APIRouter, UploadFile
from mongo import transcripts_collection
import uuid
import os
from fastapi import APIRouter,Request
from utils.voice_caller import make_voice_call
from fastapi.responses import Response

from datetime import datetime
from utils.whisper_utils import transcribe_audio_from_url
from fastapi import APIRouter, FastAPI
from fastapi.responses import Response
from utils.whisper_utils import transcribe_audio

router = APIRouter()

@router.post("/voice-upload/")
async def upload_voice(file: UploadFile):
    contents = await file.read()

    os.makedirs("recordings", exist_ok=True)
    filename = f"recordings/{uuid.uuid4().hex}.wav"
    with open(filename, "wb") as f:
        f.write(contents)

    transcript = transcribe_audio(filename)

   
    transcripts_collection.insert_one({
        "filename": filename,
        "transcript": transcript
    })

    return {"message": "Transcribed and saved", "transcript": transcript}


@router.get("/voice-transcripts/")
def get_transcripts():
    return list(transcripts_collection.find({}, {"_id": 0}))


@router.get("/call-patient/")
def trigger_voice_call():
    call_sid = make_voice_call()
    return {"message": "Voice call initiated", "call_sid": call_sid}





@router.api_route("/twiml", methods=["GET", "POST"])
async def get_twiml(request: Request):
    twiml = """
   <Response>
        <Say voice="alice">Hello, this is Setu AI calling for a follow-up.</Say>
        <Pause length="1"/>
        <Say>How are you feeling today?</Say>
        <Pause length="4"/>
        <Say>Has your condition improved since your last visit?</Say>
        <Pause length="4"/>
        <Say>Are there any side effects?</Say>
        <Pause length="4"/>
        <Say>Are you satisfied with your treatment?</Say>
        <Pause length="2"/>
        <Say>Now please say your answer after the beep.</Say>
        <Record timeout="5" maxLength="30"/>
        <Say>Thank you. Goodbye.</Say>
    </Response>
    """
    return Response(content=twiml, media_type="application/xml")


@router.post("/recording-complete",include_in_schema=False)
async def handle_recording(request: Request):
    try:
        form = await request.form()
        recording_url = form.get("RecordingUrl")
        call_sid = form.get("CallSid")
        timestamp = datetime.now().isoformat()

        if not recording_url:
            print(" No recording URL received from Twilio.")
            return {"error": "No recording URL"}

        print(" Recording URL:", recording_url)
        import time
        time.sleep(3)
        
        transcript = transcribe_audio_from_url(recording_url)

        transcripts_collection.insert_one({
            "call_sid": call_sid,
            "recording_url": recording_url,
            "timestamp": timestamp,
            "transcript": transcript
        })

        return {"message": "Transcription saved", "transcript": transcript}
    
    except Exception as e:
        print(" Error in /recording-complete:", str(e))
        return {"error": "Something went wrong"}
