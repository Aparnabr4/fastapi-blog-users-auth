from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class Login(BaseModel):
    username: str
    password: str

    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        from_attributes = True

class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        from_attributes = True

class Blog(BaseModel):
    title: str
    body: str
    user_id : int

    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
        title: str
        body: str
        creator: ShowUser


        class Config():
            from_attributes = True