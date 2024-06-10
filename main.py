from fastapi import FastAPI
from app.V1.router.user_router import router as user_router

app = FastAPI()


@app.get('/')
def index():
    return {"name":"Carlos Villarreal",
            "message":"Hola, Bienvenido a FastAPI ......"}


app.include_router(user_router)
