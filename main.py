from fastapi import FastAPI
from routers import algo_routes

# create a new app using FastAPI (Application Programming Interface)
app = FastAPI()

# define a new path
# app decorator which defines a path for the HTTP GET method
@app.get("/")
def root():
    return{"Project": "Logic Loft!"}

app.include_router(algo_routes.router)