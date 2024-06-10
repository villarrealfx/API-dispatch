from pydantic import BaseModel, Field, EmailStr

from datetime import date

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="villarreal.fx@gmail.com"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="MyTypicalUsername"
    )
    hiring_date: date = Field(
        ...,
        example=date(2024, 7, 9)
    )
    is_active:bool = Field(
        ...,
        example=True
    )
    is_staff:bool = Field(
        ...,
        example=False
    )
    

class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )

class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )
