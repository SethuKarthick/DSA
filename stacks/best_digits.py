num = "4173"
k = 2


def best_digits(num, k):

    stack = []

    for digit in num:
        while stack and k>0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0 :
        stack.pop()
        k -= 1

    return ''.join(stack)

res = best_digits(num, k)
print(res)


