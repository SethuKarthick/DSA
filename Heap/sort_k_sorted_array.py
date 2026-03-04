import heapq

def heap_sort(array, k):
    heap = array[:k+1]
    heapq.heapify(heap)

    target_idx = 0

    for i in range(k+1, len(array)):
        array[target_idx] = heapq.heappop(heap)
        target_idx += 1

        heapq.heappush(heap, array[i])

    while heap:
        array[target_idx] = heapq.heappop(heap)
        target_idx += 1

    return array

array = [3, 2, 1, 6, 5, 4, 8, 7, 5]
k = 3

res = heap_sort(array, k)
print(res)



