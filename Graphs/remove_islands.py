

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]


#
# def remove_islands(matrix):
#
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             is_row_border = row == 0 or row == len(matrix)-1
#             is_column_border = col == 0 or col == len(matrix[row]) - 1
#             is_border = is_row_border or is_column_border
#             if not is_border:
#                 continue
#             if matrix[row][col] != 1:
#                 continue
#             change_ones_connected_border_to_twos(matrix, row, col)
#
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#
#             if matrix[row][col] == 2:
#                 matrix[row][col] = 1
#             elif matrix[row][col] == 1:
#                 matrix[row][col] = 0
#     return matrix
#
#
# def change_ones_connected_border_to_twos(matrix, row, col):
#     stack = [(row, col)]
#
#     while len(stack) > 0:
#         current_i, current_j = stack.pop()
#
#         matrix[current_i][current_j] = 2
#
#         neighbours = get_neighbours(current_i, current_j, matrix)
#         for ni, nj in neighbours:
#             if matrix[ni][nj] != 1:
#                 continue
#             stack.append((ni, nj))
#
#
# def get_neighbours(i, j, matrix):
#     neighbours = []
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     if i > 0:
#         neighbours.append((i-1, j))
#     if i + 1 < rows:
#         neighbours.append((i+1, j))
#     if j > 0:
#         neighbours.append((i, j-1))
#     if j + 1 < cols:
#         neighbours.append((i, j+1))
#     return neighbours
#
# res = remove_islands(matrix)
# print(res)





def remove_islands(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Mark border-connected 1s as 2
    for row in range(rows):
        for col in range(cols):
            is_border = row == 0 or row == rows - 1 or col == 0 or col == cols - 1
            if is_border and matrix[row][col] == 1:
                change_ones_connected_border_to_twos(matrix, row, col)

    # Convert: 2 → 1 (keep), 1 → 0 (remove islands)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 2:
                matrix[row][col] = 1
            elif matrix[row][col] == 1:
                matrix[row][col] = 0

    return matrix


def change_ones_connected_border_to_twos(matrix, row, col):
    stack = [(row, col)]

    while stack:
        i, j = stack.pop()
        matrix[i][j] = 2

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == 1:
                stack.append((ni, nj))


res = remove_islands(matrix)
print(res)