from fastapi import FastAPI
from pydantic import BaseModel

from sky_ai import SkyAI
from database import init_db, save_message

app = FastAPI(title="Sky AI - Sky Plug CDM")

init_db()

class ChatRequest(BaseModel):
    user: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    ai = SkyAI(req.user)
    response = ai.respond(req.message)

    save_message(req.user, req.message, response)

    return {
        "user": req.user,
        "response": response
    }

@app.get("/")
def root():
    return {"status": "Sky AI is running 24/7 🚀"}
