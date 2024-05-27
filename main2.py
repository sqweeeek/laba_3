from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
async def read_item(name: str):
    return f"Name {name}"