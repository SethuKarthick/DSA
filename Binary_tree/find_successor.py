class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def find_successor(tree, node):
    if node.right:
        return get_left_most_node(node.right)

    return get_top_parent(node)

def get_top_parent(node):
    while node.parent and node.parent.right == node:
        node = node.parent
    return node.parent

def get_left_most_node(root):
    while root.left:
        root = root.left

    return root

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)

    root.left.parent = root
    root.right.parent = root

    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left

    node = root.left  # node with value 2
    successor = find_successor(root, node)

    print(successor.value if successor else None)