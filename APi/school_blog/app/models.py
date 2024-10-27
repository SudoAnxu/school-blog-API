from bson import ObjectId
from app.schemas import BlogPost
from pydantic import BaseModel

class BlogPostInDB(BlogPost):
    id: str

class BlogPostResponse(BlogPostInDB):
    class Config:
        orm_mode = True
