from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/items/{id}")
def testApi(id):
    return {"test": id}
