from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
from typing import List

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "llama2"  # default model
    messages: List[Message]
    stream: bool = False

@app.post("/api/chat")
async def chat_with_llm(request: ChatRequest):
    try:
        # Prepare the prompt
        prompt = "\n".join([f"{msg.role}: {msg.content}" for msg in request.messages])
        prompt += "\nassistant: "

        # Call Ollama using subprocess
        process = subprocess.Popen(
            ["ollama", "run", request.model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False  # Safe on Windows when binary is in PATH
        )

        stdout, stderr = process.communicate(input=prompt)

        if process.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Ollama error: {stderr.strip()}")

        return {"response": stdout.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/models")
async def get_available_models():
    try:
        # List available Ollama models
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True
        )
        models = [line.split()[0] for line in result.stdout.splitlines()[1:]]
        return {"models": models}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) #runs the FastAPI with uvicorn server on localhost:8000