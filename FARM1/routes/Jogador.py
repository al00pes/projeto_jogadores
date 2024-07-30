from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return " Bem vindo ao FullStack Farm"


#Lista os novos jogadores.
@jogador_router.get('/jogadores')
async def  lista_jogadores():
    return listaJogadoresEntidade(conexao.local.jogador.find()) #retorna todas as informações da coleção (mongo)

# Detalhes de um jogador - 
@jogador_router.get('/jogadores/{jogador_id}')
def busca_jogador_id(jogador_id):
    return jogadorEntidade(
        conexao.local.jogador.find_one
        (
            {"_id": ObjectId(jogador_id)} # A busca é feita pelo ID 
        )
    )

#insere novos jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador)) # Insere a informação como dicionario 
    return listaJogadoresEntidade(conexao.local.jogadores.find())

#Atualiza Jogador
@jogador_router.put('/jogadores/{jogador_id}')
async def atualiza_jogador(jogador_id,jogador: Jogador):
    conexao.local.jogador.find_one_and_update(
        {
            "_id": ObjectId(jogador_id) # Busca o ID
        },
        {
            "$set":dict(jogador) # Atualiza o id que foi buscado
        }
    )
    return jogadorEntidade(
        conexao.local.jogador.find_one
        (
            {
            "_id": ObjectId(jogador_id) #Retorna com a informação atualizada 
            }
        )
    )

#Exclusão de jogadores
@jogador_router.delete('/jogadores/{jogador_id}')
async def excluir_jogador(jogador_id):
    return jogadorEntidade(
        conexao.local.jogador.find_one_and_delete(
            {
                "_id": ObjectId(jogador_id)
            }
            
        )
    )