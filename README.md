# healthcareassisstant

This is a personal project I built to explore how AI can be used in healthcare assistance. It includes features like generating summaries from doctor notes, sending vitals charts via email/WhatsApp, and even voice call follow-ups using Twilio.

I’ve used FastAPI for the backend, and MongoDB/PostgreSQL for storing data. The project is deployed on Render and integrated with Twilio, Gmail, and OpenAI for various functionalities.

---

## 🚀 Features

- Accept doctor notes and convert them into structured health summaries
- Generate and email PDF reports of summaries
- Send summaries via WhatsApp and SMS
- Generate vitals trend chart (Plotly) and email it
- Voice call follow-ups to patients with custom messages
- Record and transcribe patient's voice responses using Whisper + Twilio
- Store everything in MongoDB and PostgreSQL

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **AI**: OpenAI Whisper API
- **Database**: MongoDB (transcripts), PostgreSQL (patients & notes)
- **Cloud**: Render (Deployment), GitHub (Storage), Firebase (optional)
- **Third-party APIs**: Twilio (SMS, WhatsApp, Voice), Gmail SMTP

---

## 🧠 What I Learned

- How to work with FastAPI and build API endpoints from scratch
- Using OpenAI APIs for audio transcription
- Handling real-time communication with Twilio
- Deploying full-stack Python projects on Render
- Managing `.env`, GitHub storage, and security properly

---

## 📁 Structure

```

healthcare-assistant/
├── main.py
├── routers/
│   └── voice.py
├── utils/
│   ├── email\_sender.py
│   ├── voice\_caller.py
│   ├── pdf\_generator.py
│   └── whisper\_utils.py
├── models.py
├── schemas.py
├── database.py
├── mongo.py
└── README.md  ← this file

```


---

## 🧪 How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
````

Go to [http://localhost:8000/docs](http://localhost:8000/docs) to try out the API.

---

## 🌍 Deployment

* Backend deployed to: [https://healthcare-assistantt.onrender.com](https://healthcare-assistantt.onrender.com)
* Static files (PDF, vitals chart): Hosted on GitHub

---

## 💌 Final Note

I learned a lot while building this. It’s not perfect, but it was a huge step for me. I built everything from scratch, faced errors, fixed them, and kept going. If you're checking this out — thank you. 💙

```

-
