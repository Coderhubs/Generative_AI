from fastapi import FastAPI


app = FastAPI()
@app.get("/")


def greeting():


    return {"message": "Hello, World from Simra!"}

