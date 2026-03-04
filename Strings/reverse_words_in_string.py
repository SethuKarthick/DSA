strings = "AlgoExpert is the best!"

def reverse_words(strings):

    string_list = strings.split(" ")

    left = 0
    right = len(string_list) - 1

    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1

    return " ".join(string_list)

res = reverse_words(strings)
print(res)
