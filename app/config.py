import os #libreria para accedere a variables de entorno en el sistema
from dotenv import load_dotenv #carga las variables de entorno que estan en el archivo .env

#aqui especificamos el archivo que tiene las variables de entorno
load_dotenv(".env.local")

class Settings: 
    #usamos el metodo os.getenv() para obtener los valores de las variables de entorno
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID")
    FIRESTORE_DATABASE_ID: str = os.getenv("FIRESTORE_DATABASE_ID")

#instanciamos la clase Settings que se usara para importar el contenido de la clase a otros proyectos
settings = Settings()
