width = 3
height = 3

def number_of_ways_to_traverse_graph(row, col):
    prev = [1] * col

    for i in range(1, row):
        current = [1] * col
        for j in range(1, col):
            current[j] = prev[j] + current[j - 1]
        prev = current
    return prev[-1]

res = number_of_ways_to_traverse_graph(width, height)
print(res) # output --> 6