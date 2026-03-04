points = [
    [1, 1],
    [2, 2],
    [3, 3],
    [3, 1],
    [4, 2],
    [5, 3]
]

def get_points_count(points):



    n = len(points)
    if n < 2:
        return n

    max_points = 0

    for i in range(n):
        slopes = {}
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]

            rise = y2 - y1
            run = x2 - x1

            slope = get_slopes(rise, run)
            if slope not in slopes:
                slopes[slope] = 1
            slopes[slope] += 1
            max_points = max(max_points, slopes[slope])


    return max_points


def get_slopes(rise, run):

    if run == 0:
        return "inf", 0

    if rise == 0:
        return 0, "inf"

    g = gcd(rise, run)
    rise //= g
    run //= g

    if run < 0:
        rise *= -1
        run *= -1

    return rise, run

def gcd(a, b):
    while b !=0:
        a, b = b, a%b
    return abs(a)

result = get_points_count(points)
print(result)
