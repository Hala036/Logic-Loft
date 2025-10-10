# worst: O(n^2) avg: O(n^2)
def insertion_sort(arr):
    n = len(arr)
    res = arr.copy()
    for i in range(n):
        for j in range(i):
            if res[i] < res[j]:
                # switch
                temp = res[i]
                res[i] = res[j]
                res[j] = temp

    return res