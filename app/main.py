from fastapi import FastAPI #importa la clase FastApi para crear la API
from fastapi.middleware.cors import CORSMiddleware #controla el acceso (CORS) de las paginas que pueden acceder a nuestra API
from app.routes.notes.endpoints import router as notes_router #direccion de los endpoints
from app.clients.firestore import get_firestore_client

#Instanciamos FastApi
app1 = FastAPI()

#configurar CORS(controlar el acceso de nuestra API)
app1.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#Permite que cualquier dominio pueda acceder a tu API.(* = todos)
    allow_credentials=True,
    allow_methods=["*"],#Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"]#Permite todos los headers personalizados enviados por el cliente(Fronted).
)
#concetamos la "mini-api"(endpoints del archivo endpoints.py) en el main 
app1.include_router(notes_router)

@app1.get("/hola")
def hello_world():
    return {"message" : "Hello world"}
