input = [5, 10, -5]


def colliding_asteriods(input):
    stack = []

    for aestroid in input:
        while stack and aestroid < 0 < stack[-1]:
            top = stack[-1]
            if abs(aestroid) > abs(top):
                stack.pop()
                continue
            elif abs(aestroid) == abs(top):
                stack.pop()
                break
            else:
                break

        else:
            stack.append(aestroid)
    return stack


res = colliding_asteriods(input)
print(res)
