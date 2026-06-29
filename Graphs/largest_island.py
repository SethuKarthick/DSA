matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

def largest_island(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False] * cols for _ in range(rows)]
    max_size = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                size = dfs(r, c, matrix, visited)
                max_size = max(max_size, size)
    return max_size

def dfs(r, c, matrix, visited):
    if r < 0  or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or visited[r][c] or matrix[r][c] == 0:
        return 0

    visited[r][c] = True
    size = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        size += dfs(r + dr, c + dc, matrix, visited)

    return size

res = largest_island(matrix)
print(res)