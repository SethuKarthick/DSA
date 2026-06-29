class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def merge_binary_tree(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1

    merged = BinaryTree(t1.value+t2.value)
    merged.left = merge_binary_tree(t1.left, t2.left)
    merged.right = merge_binary_tree(t1.right, t2.right)
    return merged


if __name__ == "__main__":

    t1 = BinaryTree(1)
    t1.left = BinaryTree(3)
    t1.right = BinaryTree(2)
    t1.left.left = BinaryTree(5)

    t2 = BinaryTree(2)
    t2.left = BinaryTree(1)
    t2.right = BinaryTree(3)
    t2.left.right = BinaryTree(4)
    t2.right.right = BinaryTree(7)

    merged = merge_binary_tree(t1, t2)


    # Simple in-order print to verify
    def inorder(node):
        if node is None:
            return []
        return inorder(node.left) + [node.value] + inorder(node.right)


    print(inorder(merged))

