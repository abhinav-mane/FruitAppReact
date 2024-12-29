from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits : List[Fruit]


origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


memory_db = {"fruits": []}

@app.get("/fruits", response_model = Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

@app.post("/add-fruits", response_model = Fruit)
def create_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0" , port=8000)