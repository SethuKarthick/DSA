n = 7
denoms = [1, 5, 10]


def min_coins(n, denoms):
    ways = [float("inf")] * (n+1)
    ways[0] = 0

    for coin in denoms:
        for amount in range(coin, n+1):
            if ways[amount - coin] != float("inf"):
                ways[amount] = min(ways[amount], ways[amount-coin] + 1)

    return ways[n] if ways[n] != float("inf") else -1

res = min_coins(n, denoms)
print(res)
