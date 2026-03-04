seats = [1,0,0,0,1,0,1]


def best_seat(seats):
    best_seat_idx = -1
    longest = 0

    n = len(seats)

    for i in range(n):
        if seats[i] == 1:
            continue

        left = i
        while left - 1 >= 0 and seats[left-1] == 0:
            left -= 1
        right = i
        while right + 1 < n and seats[right+1] == 0:
            right += 1

        current_length = right - left + 1
        if current_length > longest:
            longest = current_length
            best_seat_idx = left + current_length // 2

    return best_seat_idx

res = best_seat(seats)
print(res)

