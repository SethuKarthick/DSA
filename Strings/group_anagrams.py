words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(words):
    anagram_set = {}

    for word in words:
        char_counts = [0] * 26

        for char in word:
            char_counts[ord(char) - ord('a')] += 1
        # print(f"before tuple :: {char_counts}")
        key = tuple(char_counts)
        # print(f"key: {key}")
        if key not in anagram_set:
            anagram_set[key] = []
        anagram_set[key].append(word)

    return list(anagram_set.values())

res = group_anagrams(words)
print(res)