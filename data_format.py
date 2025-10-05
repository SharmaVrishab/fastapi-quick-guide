from fastapi import FastAPI

app = FastAPI()


@app.get("/api/data")
async def get_data():
    return {"message": "This is a GET response!"}


#  before post frontend did the preflight to check for methods {tests}
@app.post("/api/data")
async def post_data(payload: dict):
    return {"message": "POST received!", "data": payload}
