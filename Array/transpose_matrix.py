matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

def transpose(matrix):
    rows = len(matrix)
    col = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(col)]

    for i in range(col):
        for j in range(rows):
            transposed[i][j] = matrix[j][i]

    return transposed

res = transpose(matrix)
print(res)