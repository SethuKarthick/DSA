input = [4, 5, 2, 10, 8]


def next_greater_element(input):
    stack = []
    n = len(input)
    res = [-1] * n  # Initialize result array with -1

    # Traverse the array twice to handle the circular nature
    for i in range(2 * n):
        circular_idx = i % n  # Get the circular index (simulates wrapping around)

        # While stack is not empty and the current element is greater than the element at the index of the top of the stack
        while stack and input[circular_idx] > input[stack[-1]]:
            idx = stack.pop()
            res[idx] = input[circular_idx]

        # Only push indices during the first pass (i < n) to avoid overwriting
        if i < n:
            stack.append(circular_idx)

    return res


result = next_greater_element(input)
print(result)

