k = 3
tasks = [1, 3, 5, 3, 1, 4]

def task_assignment(tasks, k):
    indexed_tasks = [(task, idx) for idx, task in enumerate(tasks)]
    indexed_tasks.sort()

    pairs = []
    left = 0
    right = len(tasks) - 1

    while left < right:
        pairs.append((indexed_tasks[left][1], indexed_tasks[right][1]))
        left += 1
        right -= 1
    pair_sums = [tasks[a] + tasks[b] for a, b in pairs]
    return max(pair_sums)
    # return pairs

res = task_assignment(tasks, k)
print(res)
