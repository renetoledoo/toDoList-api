from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()


class Tarefa(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]


lista = []

@app.post("/inserir")
def inserir(tarefas: Tarefa, request):
    try:
        lista.append(tarefas)
        print(tarefas)
        return {'status': 'Criada com Sucesso'}
    except Exception as e:  #
        print(f"Erro ao cadastrar tarefa: {e}")
        return {'status': 'Tarefa não cadastrada'}


@app.post('/listar')
def listar(opcao: int = 0):
    try:
        return lista[id]
    except:
        return lista


@app.post('/alterarStatus')
def alteraStatus(id: int):
    try:
        lista[id].realizada = not lista[id].realizada
        return lista[id]
    except:
        return {'Status': 'Não foi possivel trocar status.'}

@app.post('/exlcuir')
def excluir(id: int):
    try:
        del lista[id]
        return {'Item excluido com Sucesso.'}
    except:
        return {'Não foi possível excluir o item da lista'}