class SuffixTrieNode:
    def __init__(self):
        self.children_node = {}
        self.end_word  = False

class SuffixTrie:
    def __init__(self, string):
        self.string = string
        self.root = SuffixTrieNode()
        self.build_suffix_trie()

    def build_suffix_trie(self):
        for i in range(len(self.string)):
            suffix = self.string[i:]
            self.insert_suffix(suffix)

    def insert_suffix(self, suffix):
        current_node = self.root
        for char in suffix:
            if char not in current_node.children_node:
                current_node.children_node[char] = SuffixTrieNode()
            current_node = current_node.children_node[char]
        current_node.end_word = True

    def contains(self, string_to_search):
        current_node = self.root
        for char in string_to_search:
            if char not in current_node.children_node:
                return False
            current_node = current_node.children_node[char]
        return current_node.end_word


if __name__ == "__main__":
    string_1 = "bat"
    suffix_trie = SuffixTrie(string_1)
    string_2 = "at"
    print(suffix_trie.contains(string_2))


