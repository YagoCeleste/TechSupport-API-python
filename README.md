# 🛠️ TechSupport API (FastAPI)

Uma API RESTful desenvolvida em Python com FastAPI para o gerenciamento de tickets e chamados de suporte de T.I. Este projeto simula o backend de uma aplicação Full Stack, gerenciando requisições assíncronas e operações CRUD.

## 🚀 Tecnologias
* **Python 3**
* **FastAPI:** Criação de rotas e documentação automática (Swagger UI).
* **Pydantic:** Validação de dados e tipagem estática.
* **Uvicorn:** Servidor ASGI para rodar a aplicação.

## ⚙️ Funcionalidades
* `GET /chamados`: Retorna a lista de todos os tickets de suporte.
* `POST /chamados`: Abre um novo chamado de infraestrutura ou software.
* `PUT /chamados/{id}`: Atualiza o status do chamado (ex: Resolvido).
* `DELETE /chamados/{id}`: Remove um ticket do banco de dados.

## 💻 Como executar
1. Instale as dependências: `pip install fastapi uvicorn`
2. Rode o servidor: `uvicorn main:app --reload`
3. Acesse a documentação interativa gerada automaticamente em: `http://127.0.0.1:8000/docs`
