array = [
    [0, 0, 0, 0],  # row 0
    [1, 0, 1, 0],  # row 1
    [0, 0, 0, 0]   # row 2
]
source = 1  # water starts at column 1 (second column)

def waterfall_streams(array, source):
    height = len(array)
    width = len(array[0])

    rowAbove = array[0][:]
    rowAbove[source] = -1

    for row in range(1, height):
        currentRow = array[row][:]
        for col in range(width):
            valueAbove = rowAbove[col]
            hasWaterAbove = valueAbove < 0
            hasBlock = currentRow[col] == 1

            if not hasWaterAbove:
                continue
            if not hasBlock:
                currentRow[col] += valueAbove
                continue

            split_water = valueAbove // 2
            left = col - 1
            right = col + 1

            while left >= 0:
                left -= 1
                if rowAbove[left] == 1:
                    break
                if currentRow[left] != 1:
                    currentRow[left] += split_water
                    break

            while right < width:
                right += 1
                if rowAbove[right] == 1:
                    break
                if currentRow[right] != 1:
                    currentRow[right] += split_water
                    break
        rowAbove = currentRow[:]

    final_percentages = list(map(lambda x: x * 100 if x > 0 else x*-100 if x < 0 else 0.0, rowAbove))

    return final_percentages
result = waterfall_streams(array, source)
print(result)

