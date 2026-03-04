array = [7, 6, 4, -1, 1, 2]
targetSum = 16

def four_sum(array, target_sum):
    all_pairs = {}
    quadruplets = []

    for i in range(1, len(array)):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            diff = target_sum - current_sum
            if diff in all_pairs:
                for pair in all_pairs[diff]:
                    quadruplets.append(pair + [array[i], array[j]])

        for k in range(0, i):
            pair_sum = array[k] + array[i]
            if pair_sum not in all_pairs:
                all_pairs[pair_sum] = []
            all_pairs[pair_sum].append([array[k], array[i]])

    return quadruplets

res = four_sum(array, targetSum)
print(res)

