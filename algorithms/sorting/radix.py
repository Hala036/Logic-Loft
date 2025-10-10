#O(nk)
def count_sort(res, exp):
    n = len(res)

    output = [0] * n
    count = [0] * 10

    for num in res:
        index = num // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in range(n - 1, -1, -1):
        index = res[i] // exp
        r = count[index % 10] - 1
        output[r] = res[i]
        count[index % 10] -= 1

    for i in range(0, len(res)):
        res[i] = output[i]

    res = output.copy()


def radix_sort(arr):
    exp = 1
    _max = max(arr)
    res = arr.copy()

    while _max / exp >= 1:
        count_sort(res, exp)
        exp *= 10

    return res
