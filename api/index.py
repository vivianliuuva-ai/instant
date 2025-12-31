from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"

# Vercel requires the handler to be exported
handler = Mangum(app, lifespan="off")
