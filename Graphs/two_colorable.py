edges = [
  [1],
  [0, 2],
  [1]
]

from collections import deque

def tw_colorable(edges):
    n = len(edges)
    colors = [None] * n
    colors[0] = 0
    queue = deque([0])

    while queue:
        node = queue.popleft()

        for neighbor in edges[node]:
            if colors[neighbor] is None:
                colors[neighbor] = 1 - colors[node]
                queue.append(neighbor)
            elif colors[neighbor] == colors[node]:
                return False
    return True

res = tw_colorable(edges)
print(res)
