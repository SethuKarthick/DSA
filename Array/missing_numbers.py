nums = [1, 4, 3]

def missing_nums(nums):
    n = len(nums) + 2
    actual_sum = n * (n + 1) // 2
    target_sum = sum(nums)

    missing_sum = actual_sum - target_sum

    mid = missing_sum // 2

    expected_left_sum = mid * (mid + 1) // 2
    actual_left_sum = sum(x for x in nums if x <= mid)
    missing_one = expected_left_sum - actual_left_sum

    missing_two = missing_sum - missing_one

    return [missing_one, missing_two]

res = missing_nums(nums)
print(res)
