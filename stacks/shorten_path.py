path = "/foo/../bar//baz/"

def shorten_path(path):
    starts_with_slash = path[0] == "/"
    tokens = filter(is_important, path.split("/"))
    stack = []


    if starts_with_slash:
        stack.append("")

    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)

def is_important(token):
    return len(token) > 0 and token != "."

result = shorten_path(path)
print(result)
