array = [4, 2, 1, 3, 6, 7, 8]

def longest_range(array):
    nums = {num: False for num in array}
    longest = 0
    best_pair = []

    for num in array:
        if nums[num]:
            continue
        nums[num] = True
        current_length = 1

        left = num - 1
        while left in nums and not nums[left]:
            nums[left] = True
            current_length += 1
            left -= 1

        right = num + 1
        while right in nums and not nums[right]:
            nums[right] = True
            current_length += 1
            right += 1

        if current_length > longest:
            longest = current_length
            best_pair = [left+1, right-1]

    return best_pair
res = longest_range(array)
print(res)