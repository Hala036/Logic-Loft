from fastapi import APIRouter
from algorithms.sorting.merge import merge_sort
import time
import inspect

router = APIRouter(prefix="/api/algorithms", tags=["Algorithms"])

@router.get("/sort/merge")
def sort_merge(arr: str):
    arr_list = list(map(int, arr.split(',')))

    start = time.time()
    sorted_list = merge_sort(arr_list)
    end = time.time()
    runtime = round((end - start) * 1000, 3)

    code = inspect.getsource(merge_sort)
    return {
        "algorithm: ": "Merge Sort",
        "input": arr_list, 
        "output": sorted_list,
        "runtime": runtime,
        "code": code
    }
