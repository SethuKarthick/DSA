disks = [
  [2, 1, 2],
  [3, 2, 3],
  [2, 2, 8],
  [2, 3, 4],
  [1, 3, 1],
  [4, 4, 5]
]

def build_stack(disks):
    disks.sort(key=lambda x: x[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for _ in range(len(disks))]

    max_height_idx = 0

    for i in range(1, len(disks)):
        current_disk = disks[i]
        for j in range(0, i):
            other_disk = disks[j]
            if other_disk[0] < current_disk[0] and other_disk[1] < current_disk[1] and other_disk[2] < current_disk[2]:
                if heights[i] <= current_disk[2] + heights[j]:
                    heights[i] = current_disk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[max_height_idx]:
            max_height_idx = i

    return max(heights), build_sequence(disks, sequences, max_height_idx)


def build_sequence(disks, sequences, current_idx):
    sequence = []

    while current_idx is not None:
        sequence.append(disks[current_idx])
        current_idx = sequences[current_idx]

    return list(reversed(sequence))


res = build_stack(disks)
print(res)


