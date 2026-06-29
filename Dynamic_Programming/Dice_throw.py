n = 4
faces = 2


def dice_throw(n, faces):

    ways = [0] * (n+1)
    ways[0] = 1

    for face in range(1, faces+1):
        for amount in range(face, n+1):
            ways[amount] += ways[amount - face]

    return ways[n]

res = dice_throw(n, faces)
print(res)