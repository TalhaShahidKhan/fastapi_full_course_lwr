import os
import shutil
from enum import Enum

import uvicorn
from fastapi import Cookie, FastAPI, File, Form, Header, Request, UploadFile
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    name: str
    age: int
    city: str


class CityName(str, Enum):
    Dhaka = "Dhaka"


@app.get("/path_params/{name}/{age}/{city}")
async def path_params(name: str, age: int, city: CityName):
    return {"name": name, "age": age, "city": city}


@app.get("/query_params")
async def query_params(name: str, age: int, city: str, req: Request):
    params = dict(req.query_params)
    return {"name": name, "age": age, "city": city, "params": params}


@app.post("/body_as_json")
async def body_as_json(person: Person):
    return person


@app.post("/formdata")
async def fromdata(request: Request, name: str = Form(), age: int = Form()):
    formdata = dict(await request.form())
    return {"name": name, "age": age, "formdata": formdata}


@app.post("/file_upload")
async def file_upload(my_file: UploadFile = File()):
    data = await my_file.read()
    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = f"{UPLOAD_DIR}/{my_file.filename}"

    with open(file_path, "wb") as bin_file:
        shutil.copyfileobj(my_file.file, bin_file)

    return {
        "filename": my_file.filename,
        "content_type": my_file.content_type,
        "size": len(data),
        "headers": dict(my_file.headers),
    }


@app.get("/headers")
async def getting_headers(request: Request, connection: str = Header()):
    data = dict(request.headers)
    return {"using_request": data, "using_header": connection}


@app.get("/cookies")
async def getting_cookies(request: Request, Cookie_001: str = Cookie()):
    data = dict(request.cookies)
    return {"using_request": data, "useing_cookie": Cookie_001}


# for development  server
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


# for production server run: gunicorn mian:app -w 4 -k uvicorn.workers.UvicornWorkers -b 0.0.0.0:8000
