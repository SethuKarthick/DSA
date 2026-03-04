string_one = "abc"
string_two = "abxc"

def is_one_edit(string_one, string_two):

    len1 = len(string_one)
    len2 = len(string_two)

    if abs(len1 - len2) > 1:
        return False

    s1 = string_one if len1 <= len2 else string_two
    s2 = string_two if len1 <= len2 else string_one

    i = 0
    j = 0
    found_diff = False

    while i < len(s1) and j < len(s2):

        if s1[i] != s2[j]:
            if found_diff:
                return False
            found_diff = True
            if len(s1) != len(s2):
                j+=1
                continue
        else:
            i += 1
        j += 1
    return True

result = is_one_edit(string_one, string_two)
print(result)



