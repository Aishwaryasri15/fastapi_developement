from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/posts")
async def posts():
    return {"data": "Here are all the posts"}

