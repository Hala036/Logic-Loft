from fastapi import FastAPI
from algorithms.sorting import merge_sort

# create a new app using FastAPI (Application Programming Interface)
app = FastAPI()

# define a new path
# app decorator which defines a path for the HTTP GET method
@app.get("/")
def root():
    return{"Logic": "Loft!"}

@app.get("/sort/merge")
def sort_merge(arr: str):
    arr_list = list(map(int, arr.split(',')))
    sorted_list = merge_sort(arr_list)
    return {"input": arr_list, "output": sorted_list}