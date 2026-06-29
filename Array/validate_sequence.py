array    = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def validate_sequence(array, sequence):
    array_idx = 0
    sequence_idx = 0

    while array_idx < len(array) and sequence_idx < len(sequence):
        if array[array_idx] == sequence[sequence_idx]:
            sequence_idx += 1
        array_idx += 1

    return sequence_idx == len(sequence)

res = validate_sequence(array, sequence)
print(res)