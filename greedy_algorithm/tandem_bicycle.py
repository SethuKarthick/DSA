red = [5, 5, 3, 9, 2]
blue = [3, 6, 7, 2, 1]

fastest = True

def tandem_bicycle(red, blue, fastest):
    red.sort()
    blue.sort()
    max_speed = 0

    if fastest:
        blue.reverse()

    for i in range(len(red)):
        rider_1 = red[i]
        rider_2 = blue[i]
        max_speed += max(rider_1, rider_2)
    return max_speed

res = tandem_bicycle(red, blue, fastest)
print(res)
