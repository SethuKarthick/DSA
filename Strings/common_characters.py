strings = ["abc", "bcd", "cbacc"]

def get_comon_characters(strings):
    min_freq = {}
    for char in strings[0]:
        min_freq[char] = min_freq.get(char, 0) + 1

    for string in strings[1:]:
        freq = {}

        for char in string:
            freq[char] = freq.get(char, 0) + 1

        for char in list(min_freq.keys()):
            if char in freq:
                min_freq[char] = min(freq[char], min_freq[char])
            else:
                del min_freq[char]

    result = []
    for char, count in min_freq.items():
        result.extend([char] * count)
    return result

res = get_comon_characters(strings)
print(res)
