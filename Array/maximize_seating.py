seats = [1,0,0,0,1,0,1]

def maximize_seating(seats):
    prev = -1
    max_distance = 0
    for i, seat in enumerate(seats):
        if seat == 1:
            if prev == -1:

                max_distance = i
            else:
                distance = (i - prev) // 2
                max_distance = max(max_distance, distance)
            prev = i
    return max(max_distance, len(seats) -1 - prev)

res = maximize_seating(seats)
print(res)



