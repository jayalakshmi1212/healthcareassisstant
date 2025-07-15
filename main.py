from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import SessionLocal,engine
import models
import schemas
from models import DoctorNoteModel
from schemas import DoctorNote, DoctorNoteInDB
from gpt_utils import extract_json_from_note
from utils.pdf_generator import generate_summary_pdf
from utils.whatsapp_sender import send_whatsapp_message
from utils.email_sender import send_email,send_custom_email
from utils.sms_sender import send_sms
from utils.vitals_chart import generate_vitals_graph
from routers import voice


models.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(voice.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/patients/")
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.get("/patients/")
def list_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()

@app.post("/convert-note/")
def convert_note(data: DoctorNote,db: Session = Depends(get_db)):
    parsed = extract_json_from_note(data.note)

    db_note = DoctorNoteModel(
        symptoms=", ".join(parsed["symptoms"]),
        duration=parsed["duration"],
        sugar_level_status=parsed["sugar_level_status"],
        allergies=parsed["allergies"],
        prescription=", ".join(parsed["prescription"])
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    pdf_path = generate_summary_pdf(parsed)
    pdf_url = "https://raw.githubusercontent.com/jayalakshmi1212/pdf-storage/main/summary_fb8bbd.pdf"
    send_email("jayalakshmi.jayalakshmim720@gmail.com", pdf_url)
    send_sms(
    to_number = "+918606524428", 
    message=f"🩺 Your summary: {pdf_url}"
)

    if pdf_url:
        send_whatsapp_message(f"Download your health summary here: {pdf_url}")
    else:
        send_whatsapp_message("Health summary generated, but failed to upload PDF.")
    vitals_list = [
        {"weight": 60 + i, "sugar": 90 + i * 2, "pressure": 120 + i}
        for i in range(10)
    ]
    chart_path = generate_vitals_graph(vitals_list)
    print("✅ Vitals chart saved to:", chart_path)

    chart_url = "https://jayalakshmi1212.github.io/pdf-storage/vitals_4c53e7.html"


    send_custom_email(
        "jayalakshmim720@gmail.com",
        "📊 Your Vitals Chart from Setu AI",
        f"""
        Hello,<br><br>
        Your vitals trend is ready.<br><br>
        👉 <a href="{chart_url}" target="_blank">Click here to view the chart</a><br><br>
        (This is a hosted chart. Please open in a browser.)<br><br>
        Regards,<br>
        Setu AI Team
        """
    )


   
    send_whatsapp_message(f"📊 Your vitals chart: {chart_url}")

    return db_note

    return db_note

@app.get("/doctor-notes/")
def list_notes(db: Session = Depends(get_db)):
    return db.query(models.DoctorNoteModel).all()



from routers.voice import router as voice_router
app.include_router(voice_router)

