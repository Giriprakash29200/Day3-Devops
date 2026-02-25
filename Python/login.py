from fastapi import FastAPI, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta

Algorithm = "HS256"
Access_token_minutes = 60
secretkey = "jgfsbhghdgfj"

app = FastAPI()

def create_token(username: str):
    expire_token = datetime.utcnow() + timedelta(minutes=Access_token_minutes)
    payload = {"un": username, "exp": expire_token}
    return jwt.encode(payload, secretkey, algorithm=Algorithm)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, secretkey, algorithms=[Algorithm])
        return payload["un"]
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")

@app.post("/login")
def login(username: str, password: str):
    if username == "Admin" and password == "delta24":
        token = create_token(username)
        return {"user Token": token}
    raise HTTPException(status_code=400, detail="Username or password error")

@app.get("/secure")
def secdata(token: str):
    username = verify_token(token)
    return {"Message": f"hello {username}"}