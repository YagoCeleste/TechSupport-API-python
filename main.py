from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="TechSupport API", description="API para gerenciamento de chamados de T.I.")

# Modelo de Dados (Como um chamado deve ser estruturado)
class Ticket(BaseModel):
    id: int
    titulo: str
    descricao: str
    status: str = "Aberto" # Aberto, Em Andamento, Resolvido
    prioridade: str # Baixa, Média, Alta
    data_criacao: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# "Banco de dados" em memória para demonstração
banco_de_chamados = []

# Rota GET: Listar todos os chamados
@app.get("/chamados", response_model=List[Ticket])
def listar_chamados():
    return banco_de_chamados

# Rota POST: Criar um novo chamado de T.I.
@app.post("/chamados", response_model=Ticket)
def criar_chamado(ticket: Ticket):
    for t in banco_de_chamados:
        if t.id == ticket.id:
            raise HTTPException(status_code=400, detail="ID de chamado já existe.")
    banco_de_chamados.append(ticket)
    return ticket

# Rota PUT: Atualizar o status de um chamado (ex: de Aberto para Resolvido)
@app.put("/chamados/{ticket_id}")
def atualizar_status(ticket_id: int, novo_status: str):
    for ticket in banco_de_chamados:
        if ticket.id == ticket_id:
            ticket.status = novo_status
            return {"mensagem": "Status atualizado com sucesso!", "ticket": ticket}
    raise HTTPException(status_code=404, detail="Chamado não encontrado.")

# Rota DELETE: Excluir um chamado
@app.delete("/chamados/{ticket_id}")
def deletar_chamado(ticket_id: int):
    for i, ticket in enumerate(banco_de_chamados):
        if ticket.id == ticket_id:
            del banco_de_chamados[i]
            return {"mensagem": "Chamado removido com sucesso!"}
    raise HTTPException(status_code=404, detail="Chamado não encontrado.")