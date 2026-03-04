array_list = [2, 7, 11, 15]
target_sum = 9

def two_sum(nums, target):
    look_up = {}
    for i, num in enumerate(nums):
        potential_match = target - num
        if potential_match in look_up:
            return [look_up[potential_match], i]
        look_up[num] = i
    return []

res = two_sum(array_list, target_sum)
print(res)