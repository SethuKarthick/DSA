prices = [5, 11, 3, 50, 60, 90]


def max_profit(prices, k):

    if not prices or k == 0:
        return 0

    n = len(prices)


    if k >= n//2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    dp = [[0] * n for _ in range(k+1)]

    for t in range(1, k+1):
        maxDiff = -prices[0]
        for i in range(1, n):
            dp[t][i] = max(dp[t][i-1], prices[i] + maxDiff)
            maxDiff = max(maxDiff, dp[t-1][i] - prices[i])

    return dp[k][n - 1]


res = max_profit(prices, 2)
print(res)

