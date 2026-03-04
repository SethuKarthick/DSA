words = ["apple", "appetizer", "application", "app", "apex"]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.best_freq = 0
        self.best_prefix = ""
        self.best_prefix_len = 0

    def insert(self, word):

        current_node = self.root
        prefix_len = 0
        prefix = ""

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            current_node.count += 1
            prefix_len += 1
            prefix += char

            if (current_node.count > self.best_freq) or ((current_node.count == self.best_freq) and (prefix_len > self.best_prefix_len) or
                                                         (prefix_len == self.best_prefix_len) and (prefix < self.best_prefix)):
                self.best_prefix = prefix
                self.best_prefix_len = prefix_len
                self.best_freq = current_node.count


if __name__ == "__main__":
    trie = Trie()

    for word in words:
        trie.insert(word)

    result = trie.best_prefix
    print(result)