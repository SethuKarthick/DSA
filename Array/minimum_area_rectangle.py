points = [
    [1, 1],
    [1, 3],
    [3, 1],
    [3, 3],
    [2, 2]
]

def min_area(points):
    min_area = float("inf")
    x_to_ys = {}

    for x, y in points:
        if x not in x_to_ys:
            x_to_ys[x] = []
        x_to_ys[x].append(y)

    last_x_y_pair = {}

    for x in sorted(x_to_ys.keys()):
        ys = sorted(x_to_ys[x])

        for i in range(len(ys)):
            for j in range(i+1, len(ys)):
                y1, y2 = ys[i], ys[j]

                if (y1, y2) in last_x_y_pair:
                    area = (x - last_x_y_pair[(y1, y2)]) * (y2 - y1)
                    min_area  = min(area, min_area)
                last_x_y_pair[(y1, y2)] = x
    return min_area if min_area != float("inf") else 0

res = min_area(points)
print(res)


