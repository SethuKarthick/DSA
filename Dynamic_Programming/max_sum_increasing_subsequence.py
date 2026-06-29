
arr = [8, 12, 2, 3, 15, 5, 7]

def max_increasing_subsequence(arr):

    sums = arr[:]
    sequences = [None] * len(arr)
    max_sum_idx = 0
    for i in range(len(arr)):
        current_num = arr[i]
        for j in range(0, i):
            other_num = arr[j]
            if other_num < current_num and sums[j] + current_num >= sums[i]:
                sums[i] = sums[j] + current_num
                sequences[i] = j
        if sums[i] >= sums[max_sum_idx]:
            max_sum_idx = i
    return sums[max_sum_idx], build_sequence(arr, sequences, max_sum_idx)

def build_sequence(arr, sequences, current_idx):
    sequence = []
    while current_idx is not None:
        sequence.append(arr[current_idx])
        current_idx = sequences[current_idx]
    sequence.reverse()
    return sequence


res, sequence_list = max_increasing_subsequence(arr)
print(res, sequence_list)