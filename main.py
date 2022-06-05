from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

database: List[User] = [
    User(id=UUID("869d0d6c-fff9-4d1e-8396-9cecf4eae37a"),
         first_name="Adithya",
         last_name="Satyanarayana",
         gender=Gender.male,
         roles=[Role.admin]
         ),
    User(id=UUID("6df61e7b-545b-47e2-ace3-bf4f05dc8b36"),
         first_name="Achala",
         last_name="Kaushik",
         gender=Gender.female,
         roles=[Role.user]
         )
]

# Define a route for GET request.
@app.get("/")
async def root():
    return {"msg": "Welcome! Continue exploring FastAPI"}


@app.get("/api/v1/users")
async def fetch_users():
    return database


@app.post("/api/v1/users")
async def register_users(user: User):
    database.append(user)
    return {"id": user.id}
