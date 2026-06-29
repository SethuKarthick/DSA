array = [
  [1,  3,  4],
  [2,  5,  7],
  [9,  8,  6]
]


def zigzag_traverse(arr):
    res = []
    height = len(arr) - 1
    width = len(arr[0]) - 1

    row = 0
    col = 0
    going_down = True

    while not (row == height and col == width):
        res.append(arr[row][col])

        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    res.append(arr[row][col])
    return res


result = zigzag_traverse(array)
print(result)


