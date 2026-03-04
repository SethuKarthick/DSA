import heapq


def laptop_rentals(times):
    if not times:
        return 0

    heap = []

    times.sort(key=lambda x: x[0])

    for start, end in times:

        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)

    return len(heap)

times = [
        [0, 2],
        [1, 4],
        [4, 6],
        [0, 4],
        [7, 8],
        [5, 9]
    ]

res = laptop_rentals(times)
print(res)

