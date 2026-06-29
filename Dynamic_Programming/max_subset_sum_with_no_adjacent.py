arr = [7, 10, 12, 7, 9, 14]


def max_subset_sum(arr):
    if not arr:
        return 0

    if len(arr) == 1:
        return arr[0]

    second = arr[0]
    first = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        current = max(first, second + arr[2])
        second = first
        first = current

    return first

res = max_subset_sum(arr)
print(res)