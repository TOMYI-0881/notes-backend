from fastapi import APIRouter, HTTPException #importamos APIRouter, HTTPException
from app.schemas.note import Note, CreateNote #importamos la clase der archivo shcmea.py
from app.clients.firestore import get_firestore_client #importamos la funcion del archivo firestore.py
from typing import Dict, List #anotacion de tipo type hint para documentar el tipo de retorno de al funcion
from google.cloud import firestore

#Instanciamos APIRouter
#instanciamos una clase router para manejar las rutas de las notas
router = APIRouter(prefix="/notes", tags=["notes"])

#Obtener todas las notas
@router.get("/dates", status_code=200)
async def get_notes() -> Dict[str, List[Note]]:
    db = get_firestore_client()
    #ordenar de foram descendiente
    collection_ref = db.collection("notes").order_by("updated_at", direction=firestore.Query.DESCENDING)

    notes = []

    docs = collection_ref.stream()
    for doc in docs:
        #convertimos a diccionario la coleccion obtenida en la bases da datos
        note_data = doc.to_dict()
        #convertir Firestore Timestamp a string-ISO format
        note_data["created_at"] = note_data["created_at"].isoformat()
        note_data["updated_at"] = note_data["updated_at"].isoformat()
        notes.append(note_data)
    
    return {"notes" : notes}


#Crear una nota
@router.post("", status_code=201)
async def create_note(note_data: CreateNote)-> Dict[str, Note]:
    db = get_firestore_client()
    collection_ref = db.collection("notes")

    doc_ref = collection_ref.document()
    now = firestore.SERVER_TIMESTAMP

    new_note = {
        "id": doc_ref.id,
        "title": note_data.title,
        "content": note_data.content,
        "created_at": now,
        "updated_at": now
    }

    doc_ref.set(new_note)

    doc = doc_ref.get()
    note_stored = doc.to_dict()

    return {
        "note": {
            "id": note_stored["id"],
            "title": note_stored["title"],
            "content": note_stored["content"],
            #convertir Firestore Timestamp a string-ISO format
            "created_at": note_stored["created_at"].isoformat(),
            "updated_at": note_stored["updated_at"].isoformat()
        }
    }


