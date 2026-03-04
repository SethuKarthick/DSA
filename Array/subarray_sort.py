input = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]


def subrarray_sort(input):
    smallest = float("inf")
    largest = float("-inf")
    n = len(input)

    for i in range(n):
        if is_out_of_order(i, input):
            smallest = min(smallest, input[i])
            largest = max(largest, input[i])

    if smallest == float("inf"):
        return [-1, -1]

    left = 0
    while input[left] <= smallest:
        left += 1
    right = n-1
    while input[right] >= largest:
        right -= 1

    return [left, right]


def is_out_of_order(i, input):
    if i == 0:
        return input[i] > input[i+1]
    elif i == len(input)-1:
        return input[i] < input[i-1]
    else:
        return input[i] > input[i+1] or input[i] < input[i-1]

res = subrarray_sort(input)
print(res)
