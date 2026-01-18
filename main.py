from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/posts")
async def posts():
    return {"data": "Here are all the posts"}

@app.post("/createposts")
async def create_posts(post: Post):
    print(post)
    print(post.model_dump())
    return {"message": post}