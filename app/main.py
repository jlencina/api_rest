from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/items/{item_id}")
async def read_msg(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/{item_id}")
async def read_id(item_id: int):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app)