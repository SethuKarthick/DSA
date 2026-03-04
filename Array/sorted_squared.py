input = [-7, -3, 1, 9, 22, 30]

def sorted_squared(input):
    result = [0] * len(input)

    left_idx = 0
    right_idx = len(input) - 1
    idx = len(input) - 1

    while left_idx <= right_idx:
        left_val = input[left_idx] * input[left_idx]
        right_val = input[right_idx] * input[right_idx]

        if left_val > right_val:
            result[idx] = left_val
            left_idx += 1
        else:
            result[idx] = right_val
            right_idx -= 1
        idx -= 1

    return result

res = sorted_squared(input)
print(res)
