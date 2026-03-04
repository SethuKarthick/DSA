coins = [5, 7, 1, 1, 2, 3, 22]

def non_constructible_change(coins):
    coins.sort()

    current_change = 0

    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin 
    return current_change + 1

res = non_constructible_change(coins)
print(res)
