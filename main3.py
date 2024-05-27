from fastapi import FastAPI

app = FastAPI()

Name: str = "Name"


@app.get("/users/me")
async def read_user_me():
    return f"user name: {Name}"


@app.get("/users/{name}")
async def read_user(name: str):
    Name = name
    return f"new user name: {Name}"