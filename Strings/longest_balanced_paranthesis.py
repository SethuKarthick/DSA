string = "(()())"

def longest_balanced_string(s):
    opening_count = 0
    closing_count = 0
    max_count = 0

    for char in string:
        if char == "(":
            opening_count += 1
        else:
            closing_count += 1

        if opening_count == closing_count:
            max_count = max(max_count, closing_count * 2)
        if closing_count > opening_count:
            opening_count = closing_count = 0

    opening_count = 0
    closing_count = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "(":
            opening_count += 1
        else:
            closing_count += 1
        if opening_count == closing_count:
            max_count = max(max_count, opening_count * 2)
        if opening_count > closing_count:
            opening_count = closing_count = 0

    return max_count

res = longest_balanced_string(string)
print(res)
