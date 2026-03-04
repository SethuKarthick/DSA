array = [4, 2, -3, 1, 6]

def zero_sum(input_array):
    sums_seen = set()
    current_sum = 0

    for num in input_array:
        current_sum += num

        if current_sum == 0 or current_sum in sums_seen:
            return True

        sums_seen.add(current_sum)
    return False

# result = zero_sum(array)
# print(result)

def subarray_sum_to_target_sum(input_array, target_sum):
    sums_seen = {0}
    current_sum = 0

    for num in input_array:
        current_sum += num

        if (current_sum - target_sum) in sums_seen:
            return True
        sums_seen.add(current_sum)

    return False

res = subarray_sum_to_target_sum(array, 7)
print(res)