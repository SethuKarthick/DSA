matrix = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

def count_squares(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    total = 0
    prev_row = [0] * cols

    for i in range(rows):
        current = [0] * cols
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    current[j] = 1
                else:
                    current[j] = min(prev_row[j], current[j - 1], prev_row[j-1]) + 1
                total += current[j]
        prev_row = current

    return total

result = count_squares(matrix)
print(result)


