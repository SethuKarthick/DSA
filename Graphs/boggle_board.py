words = [
    "this",
    "is",
    "a",
    "simple",
    "boggle",
    "board",
    "NOTRE-PEATED",
    "REPEATED",
    "NOTREPEATED"
]

board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
]

class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

def build_trie(words):
    root = Trie()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.word = word
    return root

def boggle_board(board):
    trie = build_trie(words)
    visited = [[False for _ in range(len(board[0]))] for row in range(len(board))]

    result = set()

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(r, c, board, trie, visited, result, directions)

    return result

def dfs(r, c, board, node, visited, result, directions):
    if (r < 0 or r >= len(board) or
            c < 0 or c >= len(board[0]) or
            visited[r][c]):
        return


    char = board[r][c]
    if char not in node.children:
        return

    visited[r][c] = True
    node = node.children[char]

    if node.word is not None:
        result.add(node.word)

    for dr, dc in directions:
        dfs(r+dr, c+dc, board, node, visited, result, directions)

    visited[r][c] = False

res = boggle_board(board)
print(list(res))



