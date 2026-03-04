array = [
  [1, 2, 3, 4],
  [12,13,14,5],
  [11,16,15,6],
  [10,9,8,7]
]

def spiral_traverse(arr):
    res = []
    startRow = 0
    endRow = len(arr)-1
    startCol = 0
    endCol = len(arr[0])-1

    while startRow <= endRow and startCol <= endCol:

        for col in range(startCol, endCol+1):
            res.append(arr[startRow][col])

        for row in range(startRow+1, endRow+1):
            res.append(arr[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            res.append(arr[endRow][col])

        for row in reversed(range(startRow+1, endRow)):
            if startCol == endCol:
                break
            res.append(arr[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return res


result = spiral_traverse(array)
print(result)

