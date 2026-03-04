nums = [2, 3, 1, -4, -4, 2]



def single_cycle_check(nums):

    nums_elements_visited = 0
    current_idx = 0

    while nums_elements_visited < len(nums):
        if nums_elements_visited > 0  and current_idx == 0:
            return False
        nums_elements_visited += 1
        current_idx = get_current_idx(current_idx,  nums)
    return current_idx == 0


def get_current_idx(current_idx, nums):
    jump = nums[current_idx]
    next_idx = (current_idx + jump) % len(nums)
    return next_idx if next_idx >= 0 else next_idx + len(nums)

res = single_cycle_check(nums)
print(res)
