import heapq

def merge_sorted_arrays(arrays):

    min_heap = []

    for array_idx in range(len(arrays)):
        first_value = arrays[array_idx][0]
        heapq.heappush(min_heap, (first_value, array_idx, 0))

    result = []

    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)
        next_idx = element_idx + 1

        if next_idx < len(arrays[array_idx]):
            next_value = arrays[array_idx][next_idx]
            heapq.heappush(min_heap, (next_value, array_idx, next_idx))

    return result

arrays = [
    [1, 5, 9],
    [2, 3, 7],
    [0, 8]
]

res = merge_sorted_arrays(arrays)
print(res)

