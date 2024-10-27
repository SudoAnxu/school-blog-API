from pydantic import BaseModel
from typing import Optional

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    published: Optional[bool] = True
