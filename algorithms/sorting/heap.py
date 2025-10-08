# O(n log n)
def heapify(arr, n, i):
    largest = i

    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    res = arr.copy()

    for i in range(n // 2 - 1, -1, -1):
        heapify(res, n, i)

    for i in range(n - 1, 0, -1):
        res[0], res[i] = res[i], res[0]
        heapify(res, i, 0)
    
    return res
