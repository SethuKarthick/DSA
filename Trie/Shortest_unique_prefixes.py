


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            current_node.count += 1

    def get_shortest_unique_prefix(self, word):

        current_node = self.root

        prefix = ""
        for char in word:
            current_node = current_node.children[char]
            prefix += char
            if current_node.count == 1:
                return prefix
        return prefix


if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "appetizer", "application", "app", "apex"]

    for word in words:
        trie.insert(word)

    result = [trie.get_shortest_unique_prefix(word) for word in words]
    print(result)
