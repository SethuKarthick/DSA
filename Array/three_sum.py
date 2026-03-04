array = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0

def three_sum(array):
    array.sort()
    triplets = []

    for i in range(len(array)-2):

        if i > 0 and array[i] == array[i-1]:
            continue

        left = i + 1
        right = len(array) -1

        while left < right:
            current_sum = array[i] + array[left] + array[right]

            if current_sum == target_sum:
                triplets.append([array[i], array[left], array[right]])

                # left_val = array[left]
                # right_val = array[right]
                # while left < right and array[left] == left_val:
                #     left += 1
                # while left < right and array[right] == right_val:
                #     right -= 1
                while left + 1 < len(array) and array[left+1] == array[left]:
                    left += 1
                while right - 1 >= 0 and array[right-1] == array[right]:
                    right -= 1
                left += 1
                right += 1

            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return triplets

res = three_sum(array)
print(res)





