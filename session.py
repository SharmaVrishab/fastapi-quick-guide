import secrets

from fastapi import Depends, FastAPI, Form, HTTPException, Request, Response, status

app = FastAPI()

# sessio cookies
session_store = {}


@app.post("/login")
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "secret":
        # create session token
        session_token = secrets.token_hex(16)

        session_store[session_token] = {"username": username}

        #  set cookie

        response.set_cookie(
            key="session_token",
            value=session_token,
            httponly=True,  # Prevent JavaScript access
            samesite="lax",  # Protect from CSRF
            secure=False,  # Change to True if using HTTPS
        )
        return {"message": "Login successfully"}
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorised"
    )


def get_current_user(request: Request):
    session_token = request.cookies.get("session_token")
    if not session_token or session_token not in session_store:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorised"
        )
    return session_store[session_token]


@app.get("/me")
async def read_me(user: dict = Depends(get_current_user)):
    return {"user": user}


@app.post("/logout")
async def logout(response: Response, user: dict = Depends(get_current_user)):
    token_to_delete = None
    for token, info in session_store.items():
        if info == user:
            token_to_delete = token
            break
    if token_to_delete:
        del session_store[token_to_delete]
    response.delete_cookie("session_token")
    return {"message": "logout completed"}
