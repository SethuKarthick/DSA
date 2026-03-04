array = [6, 5, 4, 4]

def is_monotonic(arr):

    if len(arr) <= 1:
        return True

    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i -1]:
            decreasing = False
        elif arr[i] < arr[i -1]:
            increasing = False
    return increasing or decreasing

res = is_monotonic(array)
print(res)