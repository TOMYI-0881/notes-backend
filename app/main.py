from fastapi import FastAPI #importa la clase FastApi para crear la API
from fastapi.middleware.cors import CORSMiddleware #controla el acceso de las paginas que pueden acceder a nuestra API
#from app.routes.notes.endpoints import router as notes_router #Organizacion de endpoints

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

@app1.get("/hola")
def hello_world():
    return {"message" : "Hello world"}
