

matrix = [
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
]


def squared_zeroes(arr):
    n = len(arr)

    for topRow in range(n):
        for leftCol in range(n):
            square_length = 2
            while square_length <= n - leftCol and square_length <= n - topRow:
                bottomRow = topRow + square_length - 1
                rightCol = leftCol + square_length - 1
                if is_square_of_zeroes(arr, topRow, leftCol, bottomRow, rightCol):
                    return True
                square_length += 1
    return False

def is_square_of_zeroes(arr, r1, c1, r2, c2):

    for row in range(r1, r2+1):
        if arr[row][c1] !=0 or arr[row][c2] != 0:
            return False

    for col in range(c1, c2+1):
        if arr[r1][col] != 0 or arr[r2][col] != 0:
            return False

    return True

res = squared_zeroes(matrix)
print(res)


