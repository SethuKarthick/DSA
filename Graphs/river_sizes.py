# matrix = [
#   [1, 0, 0, 1],
#   [1, 0, 1, 0],
#   [0, 1, 1, 0],
#   [0, 0, 0, 0]
# ]

def river_sizes(matrix):
    visited = [[False for _ in row] for row in matrix]

    sizes = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j] and matrix[i][j] == 1:
                size = explore_size(i, j, matrix, visited)
                sizes.append(size)

    return sizes


def explore_size(i, j, matrix, visited):
    size = 0
    stack = [(i, j)]

    while stack:
        current_i, current_j = stack.pop()
        if visited[current_i][current_j]:
            continue
        visited[current_i][current_j] = True
        if matrix[current_i][current_j] == 0:
            continue

        size += 1
        neighbours = get_new_neighbours(current_i, current_j, matrix)
        for neighbour in neighbours:
            new_i, new_j = neighbour[0], neighbour[1]
            if not visited[new_i][new_j]:
                stack.append((new_i, new_j))
    return size


def get_new_neighbours(i, j, matrix):
    neighbours = []
    row, col = len(matrix), len(matrix[0])
    if i > 0 :
        neighbours.append((i-1, j))
    if i < row -1:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < col -1:
        neighbours.append((i, j+1))
    return neighbours


matrix = [
  [1, 0, 0, 1],
  [1, 0, 1, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0]
]
res = river_sizes(matrix)
print(res)




