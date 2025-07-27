from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Automate with Kevin's AI Agent!"}

@app.post("/run-agent")
async def run_agent(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "No prompt provided")
    # Simulate response (You can add AI logic later)
    return JSONResponse(content={"response": f"Agent received your prompt: '{prompt}'"})
