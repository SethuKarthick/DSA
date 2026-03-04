input = "([])(){}(())()()"


def balanced_brackets(input):

    opening = "({["
    match = {")": "(", "}": "{", "]": "[" }
    stack = []

    for char in input:
        if char in opening:
            stack.append(char)
        elif char in match:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()

    return len(stack) == 0

res = balanced_brackets(input)
print(res)

