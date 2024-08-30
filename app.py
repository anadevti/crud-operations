from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("ebc22950-8c1b-4725-8dc2-a9f1e38ad405"),
        first_name="Ana",
        last_name="Souza",
        email="email@gmail.com",
        role=[Role.role_admin]
    ),
    User(
        id=UUID("7322233f-abfb-4768-b04e-a004ef687f61"),
        first_name="Maria",
        last_name="Silva",
        email="teste@email.com",
        role=[Role.role_user]
    ),
    User(
        id=UUID("4175ae7f-89d1-436e-928c-5ddcf5ad1f8e"),
        first_name="João",
        last_name="Santos",
        email="joaozin@gmail.com",
        role=[Role.role_prof]
    )
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return db

@app.get("/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "User not found"}

@app.post("/api/users/")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(status_code=404,
                        detail=f"User with id {id} not found!")