from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")

def index():
    return{"message": "Hello World" }

@app.get("/test")
def index():
    return {"message" : "Test API"}
    