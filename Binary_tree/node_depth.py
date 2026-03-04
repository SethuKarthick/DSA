class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def node_depth(root):
    if root is None:
        return 0

    total_depth = 0
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()
        total_depth += depth

        if node.left is not None:
            stack.append((node.left, depth+1))
        if node.right is not None:
            stack.append((node.right, depth+1))

    return total_depth

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)

    # Call function
    print(node_depth(root))