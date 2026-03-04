
distances = [5, 25, 15, 10, 15]
fuel =      [1, 2, 1, 0, 3]
mpg = 10

def valid_starting_city(distances, fuel, mpg):
    fuel_remaining = 0
    starting_city = 0

    for i in range(len(distances)):
        fuel_remaining += (fuel[i] * mpg) - distances[i]
        if fuel_remaining < 0:
            starting_city = i + 1
            fuel_remaining = 0

    return starting_city

res = valid_starting_city(distances, fuel, mpg)
print(res)

