# Gerenciamento de Usuários com FastAPI

Este projeto implementa uma API CRUD (Create, Read, Update, Delete) simples para gerenciamento de usuários usando FastAPI e Python.

## Funcionalidades

- Listar todos os usuários
- Obter um usuário específico por ID
- Adicionar um novo usuário
- Excluir um usuário

## Pré-requisitos

- Python 3.7+
- FastAPI
- Uvicorn (para executar o servidor)

## Endpoints da API

GET /: Endpoint raiz, retorna uma mensagem "Hello World"

GET /users: Recupera todos os usuários

GET /users/{id}: Recupera um usuário específico por ID

POST /api/users/: Adiciona um novo usuário

DELETE /api/users/: Exclui um usuário por ID

## Modelagem de Dados

O modelo User inclui os seguintes campos:

- id: UUID
- first_name: String (Nome)
- last_name: String (Sobrenome)
- email: String
- role: Lista de enums Role (Função)
