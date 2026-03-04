s = "ADOBECODEBANC"
t = "ABC"

def get_smallest_substring(s, t):
    target_char = get_char_counts(t)
    substring_bounds = get_substring_bounds(s, target_char)
    return get_string_from_bounds(s, substring_bounds)

def get_string_from_bounds(big_string, substring_bounds):
    start, end = substring_bounds
    if end == float("inf"):
        return ""
    return big_string[start:end+1]


def get_substring_bounds(s, target_char):
    right = 0
    left = 0
    num_unique_chars = len(target_char)
    num_unique_chars_done = 0
    substring_bounds = [0, float('inf')]
    substring_char = {}

    while right < len(s):
        right_char = s[right]
        if right_char not in target_char:
            right += 1
            continue
        increase_char(substring_char, right_char)
        if substring_char[right_char] == target_char[right_char]:
            num_unique_chars_done += 1
        while num_unique_chars_done == num_unique_chars and left <= right:
            substring_bounds = get_bounds(left, right, substring_bounds[0], substring_bounds[1])
            left_char = s[left]
            if left_char not in target_char:
                left += 1
                continue
            if substring_char[left_char] == target_char[left_char]:
                num_unique_chars_done -= 1
            decrease_char(substring_char, left_char)
            left += 1
        right += 1
    return substring_bounds

def get_bounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if (idx2 - idx1) < (idx4 - idx3) else [idx3, idx4]



def increase_char(substring_char, char):
    if char not in substring_char:
        substring_char[char] = 0
    substring_char[char] += 1

def decrease_char(substring_char, char):
    substring_char[char] -= 1

def get_char_counts(t):
    char_counts = {}
    for char in t:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


res = get_smallest_substring(s, t)
print(res)
