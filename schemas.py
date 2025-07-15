
from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    contact: str
    address: str

class DoctorNote(BaseModel):
    note: str
    
class DoctorNoteInDB(BaseModel):
    id: int
    symptoms: str
    duration: str
    sugar_level_status: str
    allergies: str
    prescription: str

    class Config:
        orm_mode = True