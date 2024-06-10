from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException



auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.get('/', status_code=status.HTTP_201_CREATED)
async def root():
    return {'message':'root del sistema de auth'}