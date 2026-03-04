buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"

def sunset_view(buildings, direction):
    res = []
    max_height = float("-inf")
    start = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1
    i = start
    while 0 <= i < len(buildings):
        height = buildings[i]
        if height > max_height:
            max_height = height
            res.append(i)
        i += step

    if direction != "WEST":
        res = res[::-1]

    return res


result = sunset_view(buildings, direction)
print(result)





