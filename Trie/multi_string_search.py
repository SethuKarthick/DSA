class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = "*"

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end = string




if __name__ == "__main__":
    trie = Trie()

    big_string = "this is a big string"
    small_strings = ["this", "big", "not", "is"]

    for small_string in small_strings:
        trie.insert(small_string)

    contained_strings = {}


    def find_small_string_in_big_string(string, start_idx, trie, contained_strings):
        current_node = trie.root
        for i in range(start_idx, len(string)):
            current_char = string[i]
            if current_char not in current_node.children:
                break
            current_node = current_node.children[current_char]

            if current_node.end != "*":
                contained_strings[current_node.end] = True

    for i in range(len(big_string)):
        find_small_string_in_big_string(big_string, i, trie, contained_strings)
    result = [string in contained_strings for string in small_strings]

    print(result)








