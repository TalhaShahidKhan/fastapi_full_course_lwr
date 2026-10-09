import uvicorn
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "hello fastapi"}


# response type
@app.get("/response-type")
async def response_type():
    name: str = "talha"
    age: int = 20
    salary: float = 30000000000000000.23
    info: dict = {"name": name, "age": age, "salary": salary}
    isObsessed: bool = True
    html = "<h1>hello world</h1>"
    # return html
    # return [name, age, salary, isObsessed, info]
    # return JSONResponse(status_code=201, content=info)
    # return HTTPException(status_code=404, detail="Not found")
    # return FileResponse(path="sample.pdf", filename="download.pdf", media_type="application/pdf")
    pass


@app.get("/response-manipulation")
async def response_manipulation(response: Response):
    response.headers["name"] = "talha"
    response.headers["key"] = "value"
    response.set_cookie(
        key="key001",
        value="value001",
        max_age=3600,
        expires=3600,
        httponly=True,
        secure=True,
        domain="localhost",
        path="/",
    )
    return JSONResponse(status_code=201, content="Demo", headers={"key": "value"})


# for development server
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


# for  production server run: gunicorn mian:app -w 4 -k uvicorn.workers.UvicornWorkers -b 0.0.0.0:8000
