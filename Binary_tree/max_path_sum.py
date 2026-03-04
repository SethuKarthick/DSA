class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_path_sum(root):
    global_max = float('-inf')

    def helper(node):
        nonlocal global_max
        if node is None:
            return 0

        left_max = max(helper(node.left), 0)
        right_max = max(helper(node.right), 0)

        current_max = node.value + left_max + right_max

        global_max = max(global_max, current_max)

        return node.value + max(left_max, right_max)

    helper(root)
    return global_max

if __name__ == "__main__":
    # Test Case 1
    root1 = BinaryTree(1)
    root1.left = BinaryTree(2)
    root1.right = BinaryTree(3)
    print(max_path_sum(root1))  # Expected: 6

    # Test Case 2
    root2 = BinaryTree(-10)
    root2.left = BinaryTree(9)
    root2.right = BinaryTree(20)
    root2.right.left = BinaryTree(15)
    root2.right.right = BinaryTree(7)
    print(max_path_sum(root2))  # Expected: 42

    # Test Case 3: Single node
    root3 = BinaryTree(5)
    print(max_path_sum(root3))  # Expected: 5

    # Test Case 4: Negative nodes
    root4 = BinaryTree(-3)
    root4.left = BinaryTree(-2)
    root4.right = BinaryTree(-1)
    print(max_path_sum(root4))  # Expected: -1


