def counting_sort_radix(arr, exp):
    n = len(arr)
    saida = [0] * n
    count = [0] * 10

    for i in arr:
        index = i // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        saida[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    return saida

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_radix(arr, exp)
        exp *= 10
    return arr
