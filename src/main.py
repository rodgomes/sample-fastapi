from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_ping():
    return {"pong": str(datetime.now())}
