from fastapi import HTTPException, status

from passlib.context import CryptContext

from app.V1.model.user_model import User as UserModel
from app.V1.utils.db import session_local
from app.V1.shema import user_shema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(user: user_shema.UserRegister):

    get_user = session_local.query(UserModel).filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
        hiring_date=user.hiring_date,
        is_active=user.is_active,
        is_staff=user.is_staff
    )

    session_local.add(db_user)
    session_local.commit()
    
    return user_shema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )