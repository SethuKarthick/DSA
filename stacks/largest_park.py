input_grid = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]


def largest_park(land):

    row = len(land)
    col = len(land[0])

    max_size = 0

    for i in range(row):
        for j in range(col):
            if land[i][j] == 1:
                max_size = max(max_size, dfs(i, j, land))

    return max_size

def dfs(i, j, land):
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    stack = [(i, j)]
    land[i][j] = 0
    size = 0

    while stack:
        x, y = stack.pop()
        size += 1
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and land[nx][ny] == 1:
                stack.append((nx, ny))
                land[nx][ny] = 0
    return size

result = largest_park(input_grid)
print(result)



# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 1, 1],
#     [0, 1, 0, 0, 1]
# ]
#
# def largest_island(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     max_size = 0
#
#     for r in range(rows):
#         for c in range(cols):
#             if matrix[r][c] == 1:
#                 size = dfs(r, c, matrix)
#                 max_size = max(max_size, size)
#     return max_size
#
# def dfs(r, c, matrix):
#     if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] == 0:
#         return 0
#
#     matrix[r][c] = 0  # Mark as visited by setting to 0
#     size = 1
#
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#     for dr, dc in directions:
#         size += dfs(r + dr, c + dc, matrix)
#
#     return size
#
# res = largest_island(matrix)
# print(res)
