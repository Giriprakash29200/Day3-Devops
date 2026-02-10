from fastapi import FastAPI
emp = [
    {'id':'1','role':'devops','salary':'80k'},
    {'id':'2','role':'junior cloud','salary':'90k'}
]

#path peramater
app = FastAPI()
@app.get("/hello/{role}")
def welcome(role):
    for e in emp:
        if e ['role'] == role:
            return e
    return "Employee details is not found"

#query perameter
@app.get("/hello")
def welcome(role):
    for e in emp:
        if e ['role'] == role:
            return e
    return "employee data unavailable"
