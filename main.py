from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import User, Gender, Role, UserUpdateRequest

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

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in database:
        if user.id == user_id:
            database.remove(user)
            return

    raise HTTPException(
        status_code=404,
        detail=f"User ID {user_id} does not exist in the database."
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in database:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    
    raise HTTPException(
        status_code=404,
        detail=f"User ID {user_id} does not exist in the database."
    )