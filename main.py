from fastapi import FastAPI

# create a new app using FastAPI (Application Programming Interface)
app = FastAPI()

# define a new path
# app decorator which defines a path for the HTTP GET method
@app.get("/")
def root():
    return{"Logic": "Loft!"}