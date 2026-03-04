dishes = [-5, -2, 3, 8, 10]
target = 6

def sweets_and_savory(dishes, target):
    dishes.sort()
    best_diff =  float("inf")
    best_pair = [-1, -1]

    left = 0
    right = len(dishes)-1

    while left < right:
        current_sum = dishes[left] + dishes[right]

        if current_sum > target:
            right -= 1
        else:
            diff = target - current_sum
            if diff < best_diff:
                best_diff = diff
                best_pair = [dishes[left], dishes[right]]
            left += 1

    return best_pair

res = sweets_and_savory(dishes, target)
print(res)
