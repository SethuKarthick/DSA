arr = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]


def min_number_of_jumps(arr):
    max_reach = arr[0]
    steps = arr[0]

    jumps = 0

    for i in range(1, len(arr)-1):
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i

    return jumps + 1

res = min_number_of_jumps(arr)
print(res)


