# worst: O(n^2) avg: O(n^2)
def bubble_sort(arr):
    n = len(arr)
    res = arr.copy()
    for i in range(n):
        for j in range(n - i - 1):
            if res[j] > res[j + 1]:
                # switch
                res[j], res[j + 1] = res[j + 1], res[j]

    return res