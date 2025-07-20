from sqlalchemy.orm import Session, joinedload
from .. import models, schemas
from fastapi import HTTPException, Depends
from app.OAuth2 import get_current_user


def create(request, db:Session):
    new_blog = models.Blog(title=request.title, body= request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db: Session):
    blog = db.query(models.Blog).all()
    return blog


def get_by_id(id, db:Session):
    blog = db.query(models.Blog).options(joinedload(models.Blog.creator)).filter(models.Blog.id == id).all()
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Not found")


def delete(id: int, db:Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete()
    db.commit()
    return {f"Blog with the id {id} was deleted"}


def update(id, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")

    blog.update({
        models.Blog.title: request.title,
        models.Blog.body: request.body,
    })
    db.commit()
    return {f"message": f"Blog with id {id} was updated successfully"}