words = ["diaper", "repaid", "test", "abc", "cba", "tacocat"]

def semordnilap(words):
    word_set = set(words)
    result = []

    for word in words:
        reversed_word = word[::-1]

        if reversed_word in word_set and reversed_word != word:
            result.append([word, reversed_word])
            word_set.remove(reversed_word)
            word_set.remove(word)

    return result

res = semordnilap(words)
print(res)
