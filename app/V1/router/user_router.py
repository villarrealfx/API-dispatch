from fastapi import APIRouter, Depends, Body, status

from app.V1.shema import user_shema
from app.V1.service import user_service

from app.V1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_shema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user ):  # : user_shema.UserRegister = Body(...))
    """
    ## Create a new user in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return user_service.create_user(user)