from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi.security import  OAuth2PasswordRequestForm
from app.repository.login import login_user

router = APIRouter(tags=['Authentication'],prefix='/login')

@router.post('/', status_code=201)
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    return login_user(request,db)