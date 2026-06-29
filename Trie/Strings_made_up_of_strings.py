words = ["ab", "abc", "cd", "def", "abcd"]
string = "abcdef"


def strings_made_up_of_strings(words, string):
    word_set = set(words)
    n = len(string)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n+1):
        for word in word_set:
            w = len(word)

            if i>= w and dp[i-w] and string[i-w : i] == word:
                dp[i] = True
                break

    return dp[n]

res = strings_made_up_of_strings(words, string)
print(res)


# using Trie along with DP

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         current_node = self.root
#
#         for char in word:
#             if char not in current_node.children:
#                 current_node.children[char] = TrieNode()
#             current_node = current_node.children[char]
#             current_node.end = True
#
#
#
# if __name__ == "__main__":
#     words = ["ab", "abc", "cd", "def", "abcd"]
#     target = "abcdef"
#
#     trie = Trie()
#     for word in words:
#         trie.insert(word)
#
#     n = len(target)
#
#     dp = [False] * (n+1)
#     dp[0] = True
#     for i in range(n):
#         if not dp[i]:
#             continue
#         node = trie.root
#         j = i
#
#         while j < n and target[j] in node.children:
#             node = node.children[target[j]]
#             j += 1
#
#             if node.end:
#                 dp[j] = True
#     print(dp[n])
