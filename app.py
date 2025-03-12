from fastapi import FastAPI
from app import app  # Instead of 'app', use the actual filename without ".py"

app = FastAPI()
# In-memory storage for users
users = {1:{"id": 1, "name": "John"}}
@app.get("/")
def home():
    return {"message": "harishta is good girl"}






