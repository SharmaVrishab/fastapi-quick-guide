from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from frontend origin
origins = [
    "http://127.0.0.1:5500"  # frontend server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],  # GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)


@app.get("/api/data")
async def get_data():
    return {"message": "This is a GET response!"}


#  before post frontend did the preflight to check for methods {tests}
@app.post("/api/data")
async def post_data(payload: dict):
    return {"message": "POST received!", "data": payload}
