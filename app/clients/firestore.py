from google.cloud import firestore #esta dependencia nos conecta con google cloud firestoreDB
from app.config import settings #importamos la el objeto settings del archivo config que esta en la carpeta app

#pasamos los valores obtenidos del arhivo config.py
project_id = settings.GCP_PROJECT_ID
database_id = settings.FIRESTORE_DATABASE_ID

#en estos condicionales usamos la plabra not para evitar los valores falsy 
if not project_id:
    raise ValueError("GCP_PROJECT_ID is not configured")

if not database_id:
    raise ValueError("FIRESTORE_DATABASE_ID is not configured")

#aqui hacemos la conexion a la base de datos firestore
client = firestore.Client(project= project_id, database= database_id)

#creamos metodo para retornar client
def get_firestore_client():
    return client