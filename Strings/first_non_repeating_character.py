string = "abcdcaf"

def get_duplicate(string):

    char_counts = {}

    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in string:
        if char_counts[char] == 1:
            return char

    return "-"

res = get_duplicate(string)
print(res)