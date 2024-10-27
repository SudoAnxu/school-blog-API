from fastapi import APIRouter, HTTPException
from app.database import database
from app.schemas import BlogPost
from app.models import BlogPostInDB
from bson import ObjectId

router = APIRouter()

@router.post("/blogposts/", response_model=BlogPostInDB)
async def create_blog_post(blog_post: BlogPost):
    new_post = blog_post.dict()
    result = await database["blogposts"].insert_one(new_post)
    new_post["id"] = str(result.inserted_id)
    return new_post

@router.get("/blogposts/{post_id}", response_model=BlogPostInDB)
async def get_blog_post(post_id: str):
    post = await database["blogposts"].find_one({"_id": ObjectId(post_id)})
    if post is not None:
        return BlogPostInDB(**post)
    raise HTTPException(status_code=404, detail="Blog post not found")

# Additional routes (e.g., update, delete) can be added here
