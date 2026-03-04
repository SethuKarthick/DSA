nums = [2, 3, -2, 4]

def max_product(nums):

    current_max = current_min = res = nums[0]

    for num in nums[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        res = max(res, current_max)

    return res

result = max_product(nums)
print(result)
