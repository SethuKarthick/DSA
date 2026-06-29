arr = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]


def get_longest_increasing_subsequence(arr):
    n = len(arr)
    lengths = [1] * n
    sequences = [None] * n
    max_length_idx = 0

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] > lengths[max_length_idx]:
            max_length_idx = i

    return build_sequence(arr, sequences, max_length_idx)


def build_sequence(arr, sequences, current_idx):
    sequence = []

    while current_idx is not None:
        sequence.append(arr[current_idx])
        current_idx = sequences[current_idx]

    return list(reversed(sequence))

res = get_longest_increasing_subsequence(arr)
print(res)