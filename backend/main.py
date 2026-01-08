from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def get_ping():
    return {"status": "pong"}
