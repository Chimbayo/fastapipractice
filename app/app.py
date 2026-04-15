from fastapi import fastapi

app= FastAPI()

@app.get("/hello_world")
def helllo_world():
    return {"message" "Hello World"}