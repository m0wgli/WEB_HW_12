from datetime import date
from pydantic import BaseModel, Field
from datetime import datetime


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date


class ContactResponse(ContactBase):
    first_name: str = "Jonh"
    last_name: str = "Wick"
    email: str = "JW@continental.com"
    phone_number: str = "4124478554"
    birthday: date = date(year=1983, month=10, day=14)

    class Config:
        from_attributes = True
