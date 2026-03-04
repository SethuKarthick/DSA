nums = [2, 2, 1, 1, 1, 2, 2]

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if candidate == num else -1

    return candidate

res = majority_element(nums)
print(res)
