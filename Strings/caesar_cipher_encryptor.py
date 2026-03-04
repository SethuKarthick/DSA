string = "xyz"
key = 2

def decrypt(string, key):
    new_key = key % 26
    new_letters = []

    for char in string:
        new_letters.append(get_new_char(char, new_key))

    return "".join(new_letters)

def get_new_char(char, new_key):
    new_char = ord(char) + new_key

    if new_char <= ord('z'):
        return chr(new_char)
    else:
        return chr(ord('a') + (new_char - ord('z') - 1))

res = decrypt(string, key)
print(res)