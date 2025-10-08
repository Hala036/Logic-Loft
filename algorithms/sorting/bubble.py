# O(n^2)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i):
            if arr[i] > arr[j]:
                # switch
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr