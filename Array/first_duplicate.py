array = [2, 1, 5, 2, 3, 3, 4]

def first_duplicate(array):
    for num in array:

        abs_num = abs(num)
        if array[abs_num-1] < 0:
            return abs_num
        array[abs_num-1] *= -1
    return -1

res = first_duplicate(array)
print(res)

