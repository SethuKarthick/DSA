arr = [3, 6, 1, -3, 2, 7]

# expression = (a+b-c+d)

def maximize_expression(arr):
    n = len(arr)
    if n < 4:
        return 0

    max_a = [float("-inf")] * n
    max_ab = [float("-inf")] * n
    max_abc = [float("-inf")] * n
    max_abcd = [float("-inf")] * n

    for i in range(1, n):
        max_a[i] = max(max_a[i-1],  arr[i])

    for i in range(1, n):
        max_ab[i] = max(max_ab[i-1], max_a[i-1] - arr[i])

    for i in range(1, n):
        max_abc[i] = max(max_abc[i-1], max_ab[i-1] + arr[i])

    for i in range(1, n):
        max_abcd[i] = max(max_abcd[i-1], max_abc[i-1] - arr[i])

    return max_abcd[-1]

res = maximize_expression(arr)
print(res)

