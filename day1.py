import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "hello fastapi"}


# for production server
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


# for development server run: gunicorn mian:app -w 4 -k uvicorn.workers.UvicornWorkers -b 0.0.0.0:8000
