from fastapi import FastAPI

app = FastAPI()

@app.get("/health_check")
def Test():
    return {"message":"healthy !!"}
    