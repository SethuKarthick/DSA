str = "clementiscap"

def longest_string_without_duplication(str):

    last_seen = {}
    start_idx = 0
    longest = [0, 1]

    for i, char in enumerate(str):
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char]+1)
        if (i + 1) - start_idx > longest[1] - longest[0]:
            longest = [start_idx, i+1]
        last_seen[char] = i

    return str[longest[0]:longest[1]]

result = longest_string_without_duplication(str)
print(result)

