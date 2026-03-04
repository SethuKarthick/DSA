queries = [3, 2, 1, 2, 6]

def minimumWaitingTime(queries):
    queries.sort()
    total_wait_time= 0


    for i in range(len(queries)):
        duration = queries[i]
        # why queries left
        # Only one query runs at a time.
        # Each query waits for all previous queries to finish.
        queries_left = len(queries) - (i + 1)

        total_wait_time += duration * queries_left

    return total_wait_time

res = minimumWaitingTime(queries)
print(res)