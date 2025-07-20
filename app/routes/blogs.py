from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas
from app.repository.blogs import get_all, get_by_id, create, delete, update
from typing import List
from app.database import get_db
from app.OAuth2 import get_current_user

# Initialize the API router for blog-related endpoints
router = APIRouter(tags=['blog'], prefix="/blog")


# Create a new blog
@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return create(request, db)


# Fetch all blogs
@router.get('/fetch',status_code=200, response_model=List[schemas.ShowBlog])
def fetch_blog(db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return get_all(db)


# Fetch a single blog by ID
@router.get('/{id}', response_model=List[schemas.ShowBlog])
def show_by_id(id: int, db: Session = Depends(get_db),  current_user: schemas.User = Depends(get_current_user)):
    return get_by_id(id, db)


# Update a blog by ID
@router.put('/{id}/update', status_code=status.HTTP_200_OK)
def update_blog(id, request: schemas.Blog, db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return update(id, request, db)


# Delete a blog by ID
@router.delete('/{id}/delete',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return delete(id,db)


