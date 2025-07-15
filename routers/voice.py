from fastapi import APIRouter, UploadFile
from mongo import transcripts_collection
import uuid
import os
from fastapi import APIRouter,Request
from utils.voice_caller import make_voice_call
from fastapi.responses import Response


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

    # 🧠 Transcribe using Whisper API
    transcript = transcribe_audio(filename)

    # 💾 Save to MongoDB
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
        <Gather input="speech dtmf" timeout="10" numDigits="1">
            <Say voice="alice">Hello, this is Setu AI calling for a follow-up.</Say>
            <Pause length="1"/>
            <Say>How are you feeling today?</Say>
            <Pause length="4"/>
            <Say>Has your condition improved since your last visit?</Say>
            <Pause length="4"/>
            <Say>Are there any side effects?</Say>
            <Pause length="4"/>
            <Say>Are you satisfied with your treatment?</Say>
            <Pause length="4"/>
            <Say>Thank you. Goodbye.</Say>
        </Gather>
    </Response>
    """
    return Response(content=twiml, media_type="application/xml")