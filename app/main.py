from fastapi import FastAPI
from . import schemas, models
from .database import engine
from app.routes import users, blogs, authentication

# Initialize FastAPI app instance
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(engine)

# Include routes
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blogs.router)

#Vriddhi@123
# "email": "vriddhi@gmail.com"