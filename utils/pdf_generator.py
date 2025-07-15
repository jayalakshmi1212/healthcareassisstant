
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import uuid

def generate_summary_pdf(data: dict, filename: str = None) -> str:
    if not filename:
        filename = f"summary_{uuid.uuid4().hex[:6]}.pdf"

    filepath = os.path.join("pdfs", filename)
    os.makedirs("pdfs", exist_ok=True)

    c = canvas.Canvas(filepath, pagesize=letter)
    c.setFont("Helvetica", 12)

    y = 750
    c.drawString(50, y, "🩺 Healthcare Assistant - Patient Summary")
    y -= 30

    for key, value in data.items():
        value_str = ", ".join(value) if isinstance(value, list) else value
        c.drawString(50, y, f"{key.capitalize()}: {value_str}")
        y -= 20

    c.save()
    return filepath
