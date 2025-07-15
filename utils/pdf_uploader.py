# utils/pdf_uploader.py

import requests

def upload_pdf_to_fileio(filepath):
    with open(filepath, "rb") as f:
        response = requests.post("https://file.io", files={"file": f})

    try:
        data = response.json()
        return data.get("link")
    except Exception as e:
        print("❌ Upload failed. Raw response:", response.text)
        print("❌ Error:", e)
        return None
