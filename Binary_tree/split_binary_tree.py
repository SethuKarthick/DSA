class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def split_binary_tree(root, v):
    if root is None:
        return None, None


    if root.value <= v:
        left_sub_tree, right_sub_tree = split_binary_tree(root.right, v)
        root.right = left_sub_tree
        return root, right_sub_tree
    else:
        left_sub_tree, right_sub_tree = split_binary_tree(root.left, v)
        root.left = right_sub_tree
        return left_sub_tree, root

if __name__ == "__main__":
    # Build BST
    root = BinaryTree(4)
    root.left = BinaryTree(2)
    root.right = BinaryTree(6)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(3)
    root.right.left = BinaryTree(5)
    root.right.right = BinaryTree(7)

    # Split
    leftTree, rightTree = split_binary_tree(root, 3)

    # Simple inorder print to verify
    def inorder(node):
        return inorder(node.left) + [node.value] + inorder(node.right) if node else []

    print("Tree ≤ 3:", inorder(leftTree))   # [1, 2, 3]
    print("Tree > 3:", inorder(rightTree))  # [4, 5, 6, 7]