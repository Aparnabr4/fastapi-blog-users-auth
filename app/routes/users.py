from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.repository.users import get_all, get_by_id, create
from typing import List
from app.database import get_db
from app.OAuth2 import get_current_user

router = APIRouter(tags=['user'], prefix="/user")

@router.post('/create', status_code=201)
def create_user(request: schemas.User, db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return create(request, db)


@router.get('/fetch/{id}',status_code = 200, response_model=schemas.ShowUser)
def fetch_user_by_id(id, db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
   return get_by_id(id,db)

@router.get('/fetch',status_code = 200, response_model=List[schemas.ShowUser])
def fetch_user(db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return get_all(db)
