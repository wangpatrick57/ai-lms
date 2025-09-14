from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, world!"}

def main():
    # Render injects the PORT envvar.
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
