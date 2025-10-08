from fastapi import APIRouter
from algorithms.sorting.merge import merge_sort
from algorithms.sorting.bubble import bubble_sort
from algorithms.sorting.insertion import insertion_sort
from algorithms.sorting.quick import quick_sort
from algorithms.sorting.heap import heap_sort
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

@router.get("/sort/bubble")
def sort_merge(arr: str):
    arr_list = list(map(int, arr.split(',')))

    start = time.time()
    sorted_list = bubble_sort(arr_list)
    end = time.time()
    runtime = round((end - start) * 1000, 3)

    code = inspect.getsource(bubble_sort)
    return {
        "algorithm: ": "Bubble Sort",
        "input": arr_list, 
        "output": sorted_list,
        "runtime": runtime,
        "code": code
    }

@router.get("/sort/insertion")
def sort_merge(arr: str):
    arr_list = list(map(int, arr.split(',')))

    start = time.time()
    sorted_list = insertion_sort(arr_list)
    end = time.time()
    runtime = round((end - start) * 1000, 3)

    code = inspect.getsource(insertion_sort)
    return {
        "algorithm: ": "Insertion Sort",
        "input": arr_list, 
        "output": sorted_list,
        "runtime": runtime,
        "code": code
    }


@router.get("/sort/quick")
def sort_merge(arr: str):
    arr_list = list(map(int, arr.split(',')))

    start = time.time()
    sorted_list = quick_sort(arr_list)
    end = time.time()
    runtime = round((end - start) * 1000, 3)

    code = inspect.getsource(quick_sort)
    return {
        "algorithm: ": "Quick Sort",
        "input": arr_list, 
        "output": sorted_list,
        "runtime": runtime,
        "code": code
    }

@router.get("/sort/heap")
def sort_merge(arr: str):
    arr_list = list(map(int, arr.split(',')))

    start = time.time()
    sorted_list = heap_sort(arr_list)
    end = time.time()
    runtime = round((end - start) * 1000, 3)

    code = inspect.getsource(heap_sort)
    return {
        "algorithm: ": "Heap Sort",
        "input": arr_list, 
        "output": sorted_list,
        "runtime": runtime,
        "code": code
    }
