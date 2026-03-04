class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def balanced_binary_tree(root):
    return dfs(root)[1]


def dfs(node):
    if node is None:
        return 0, True

    left_height, left_balanced = dfs(node.left)
    right_height, right_balanced = dfs(node.right)

    current_height =  1+ max(left_height,right_height)
    is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

    return current_height, is_balanced

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)

    print(balanced_binary_tree(root))  # True

    root.left.left.left = BinaryTree(7)
    root.left.left.left.left = BinaryTree(8)
    print(balanced_binary_tree(root))  # False
