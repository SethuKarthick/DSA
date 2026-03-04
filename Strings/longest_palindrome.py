string = "abaxyzzyxf"

def longest_palindrome(string):
    longest = [0, 1]

    for i in range(1, len(string)):
        odd = get_palindrome_length(string, i-1, i+1)
        even = get_palindrome_length(string, i-1, i)
        current_long = max(odd, even, key= lambda x : x[1] - x[0])
        longest = max(longest, current_long, key = lambda x : x[1] - x[0])
    return string[longest[0]:longest[1]]

def get_palindrome_length(string, left, right):
    while left >= 0  and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left +1, right]

res = longest_palindrome(string)
print(res)

