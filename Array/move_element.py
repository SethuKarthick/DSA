nums = [2, 1, 2, 3, 4, 2, 5]
toMove = 2

def move_element(array, toMove):

    left = 0
    right = 0

    while right < len(array):
        if array[right] != toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
        right += 1
    return array

res = move_element(nums, 2)
print(res)
