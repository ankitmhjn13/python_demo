from fastapi import FastAPI


app = FastAPI()


@app.get("/message")
def message():
    return "hello world"