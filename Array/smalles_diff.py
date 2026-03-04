arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

def smallest_difference(array_one, array_two):
    smallest_pair = []
    smallest = float("inf")
    array_one.sort()
    array_two.sort()

    array_one_idx = 0
    array_two_idx = 0

    while array_one_idx < len(array_one) and array_two_idx < len(array_two):
        first_num = array_one[array_one_idx]
        second_num = array_two[array_two_idx]

        if first_num > second_num:
            current_sum = first_num - second_num
            array_two_idx += 1
        elif second_num > first_num :
            current_sum = second_num - first_num
            array_one_idx += 1
        else:
            return [first_num, second_num]

        if current_sum < smallest:
            smallest = current_sum
            smallest_pair = [first_num, second_num]

    return smallest_pair

res = smallest_difference(arrayOne, arrayTwo)
print(res)