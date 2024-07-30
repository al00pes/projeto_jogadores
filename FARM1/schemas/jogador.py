def jogadorEntidade(db_item) -> dict:
    return {
        "id": str(db_item['_id']),
        "nome": str(db_item["jogador_nome"]),
        "idade": int(db_item["jogador_idade"]),
        "time": str(db_item["jogador_time"]),
    }

def listaJogadoresEntidade(db_item_lista) -> list:
    lista_jogadores = []
    for item in db_item_lista:
        lista_jogadores.append(jogadorEntidade(item))
    return lista_jogadores