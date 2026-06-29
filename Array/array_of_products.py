array = [5, 1, 4, 2]

# output = [8, 40, 10, 20]

def array_of_products(array):

    products = [1 for _ in range(len(array))]

    left_running = 1
    for i in range(len(array)):
        products[i] = left_running
        left_running *= array[i]

    right_running = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running
        right_running *= array[i]

    return products
result = array_of_products(array)
print(result)
