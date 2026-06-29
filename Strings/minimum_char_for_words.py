words = ["this", "that", "did", "deed", "them!", "a"]

def minimum_char_for_words(words):

    max_freq = {}

    for word in words:

        char_freq = get_char_freq(word)
        max_freq = update_max_freq(char_freq, max_freq)

    print(max_freq)

    result = []
    for char, freq in max_freq.items():
        result.extend([char] * freq)
    return result

def update_max_freq(char_freq, max_freq):

    for char in char_freq:
        freq = char_freq[char]

        if char in max_freq:
            max_freq[char] = max(max_freq[char], freq)
        else:
            max_freq[char] = freq
    return max_freq

def get_char_freq(word):
    char_freq = {}
    for char in word:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

ress = minimum_char_for_words(words)
print(ress)
