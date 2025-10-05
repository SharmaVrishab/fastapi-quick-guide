from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# handling client errors


@app.exception_handler(HTTPException)
async def global_http_exception_handler(request: Request, exc: HTTPException):
    """
    This handler catches all HTTPException errors and returns
    a consistent JSON response.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "status_code": exc.status_code,
            "message": exc.detail,
            "path": str(request.url),
        },
    )


@app.get("/bad_request")
async def bad_request_def():
    raise HTTPException(
        status_code=400,
        detail="bad request ",
    )


@app.get("/unauthorized")
async def unauthorized_def():
    raise HTTPException(
        status_code=401,
        detail="Unauthorized",
    )


@app.get("/forbidden")
async def forbidden_def():
    raise HTTPException(
        status_code=403,
        detail="forbidden",
    )


@app.get("/rate_limit")
async def rate_limit_def():
    raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")
