from fastapi import FastAPI
from . import models
from .database import engine
from .routers import questions, users, auth
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#include the routes
app.include_router(questions.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return{"message": "Welcome to My API"}


