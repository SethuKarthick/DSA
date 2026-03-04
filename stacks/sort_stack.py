stack = [3, 1, 4, 2]

def sort_stack(stack):
    if not stack:
        return stack

    top = stack.pop()
    sort_stack(stack)
    insert_value(stack, top)
    return stack

def insert_value(stack, value):
    if not stack or value >= stack[-1]:
        stack.append(value)
        return

    top = stack.pop()
    insert_value(stack, value)
    stack.append(top)

res = sort_stack(stack)
print(res)


