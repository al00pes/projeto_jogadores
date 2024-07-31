from fastapi import FastAPI
from routes.Jogador import jogador_router
from fastapi.middleware.cors import CORSMiddleware

client_app = [
    "http://localhost:3000" #porta padrão que o react é inicializado
]

app = FastAPI()

app.include_router(jogador_router)

#Os clientes que estão permitido o acesso
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_app,
    allow_credentials=True,
    allow_methods=["*"], #acesso a todos os metodos
    allow_headers=["*"], # Acesso a todos os cabeçalhos
),