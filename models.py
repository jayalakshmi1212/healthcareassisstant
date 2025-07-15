# models.py

from sqlalchemy import Column, Integer, String
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    contact = Column(String)
    address = Column(String)

from sqlalchemy import Text

class DoctorNoteModel(Base): 
    __tablename__ = "doctor_notes"

    id = Column(Integer, primary_key=True, index=True)
    symptoms = Column(Text)
    duration = Column(String)
    sugar_level_status = Column(String)
    allergies = Column(String)
    prescription = Column(Text)