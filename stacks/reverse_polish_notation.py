expression = ["2", "1", "+", "3", "*"]


def reverse_polish_notation(expression):

    stack = []

    operations = {
        "+": lambda a, b : a+b,
        "-": lambda a, b : a-b,
        "*": lambda a, b : a*b,
        "/": lambda a, b : int(a/b),
    }

    for token in expression:
        if token in operations:
            b = stack.pop()
            a = stack.pop()
            stack.append(operations[token](a, b))
        else:
            stack.append(int(token))
    return stack.pop()

res = reverse_polish_notation(expression)
print(res)