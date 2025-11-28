from pydantic import BaseModel #poder estructurar la informacion 
from datetime import datetime #usar referencias dateTime
#from typing import Optional #crear valores por defecto

#organizamos los datos que se enviaran a la base de datos con pydantic
class Note(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

class CreateNote(BaseModel):
    title: str
    content: str