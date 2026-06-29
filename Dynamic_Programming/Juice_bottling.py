
prices = [1, 5, 8, 9, 10, 17, 17, 20]

# def get_max_profit(prices):
#     n = len(prices)
#     profits = prices[:]
#     sequences = [None for _ in range(n)]
#
#     max_profit_idx = 0
#
#     for i in range(1, n):
#         current_price = prices[i]
#
#         for j in range(0, i):
#             other_price = prices[j]
#
#             if profits[i] < profits[j] + prices[i-j-1]:
#                 profits[i] = profits[j] + prices[i-j-1]
#                 sequences[i] = j
#
#         if profits[i] >= profits[max_profit_idx]:
#             max_profit_idx = i
#
#     return profits[max_profit_idx], build_sequence(sequences, max_profit_idx)
#
#
# def build_sequence(sequences, current_idx):
#     result = []
#
#     while current_idx is not None:
#         result.append(current_idx + 1)  # bottle size (1-based)
#         current_idx = sequences[current_idx]
#
#     return result
#
# res = get_max_profit(prices)
# print(res)


def get_max_profit(prices):
    n = len(prices)
    profit = [0] * (n+1)

    for i in range(1, n+1):
        profit[i] = prices[i-1]
        for j in range(1, i):
            profit[i] = max(profit[i], profit[j] + profit[i-j])

    return profit[n]

res = get_max_profit(prices)
print(res)