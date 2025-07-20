from fastapi import HTTPException, status
from app.hashing import Hash
from app import schemas, models
from app.JWTtoken import create_access_token


def login_user(request: schemas.Login , db):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Invalid Credentials")

    if not Hash.verify(request.password, user.password,):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token" :access_token, "token_type" :"bearer"}