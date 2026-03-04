class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def symmetric_tree(tree):
    return is_mirror(tree.left, tree.right)

def is_mirror(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    if left.value != right.value:
        return False

    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

if __name__ == "__main__":
    # root = BinaryTree(1)
    # print(symmetric_tree(root))  # True
    root = BinaryTree(1)

    root.left = BinaryTree(2)
    root.right = BinaryTree(2)

    root.left.right = BinaryTree(3)
    root.right.right = BinaryTree(3)

    print(symmetric_tree(root))  # False