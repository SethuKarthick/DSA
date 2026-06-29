n = 6
denoms = [1, 5]


def num_ways(n, denoms):
    ways = [0] * (n+1)
    ways[0] = 1

    for coin in denoms:
        for amount in range(coin, n+1):
            ways[amount] += ways[amount-coin]

    return ways[n]

res = num_ways(n, denoms)
print(res)