from app.hashing import Hash
from .. import models, schemas
from fastapi import HTTPException, status

def create(request, db):
    new_user = models.User(name=request.name, email = request.email,  password=Hash.bcrypting((request.password)))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_by_id(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")


def get_all(db):
    user = db.query(models.User).all()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users not found")