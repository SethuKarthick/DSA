class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree(root):
    if root is None:
        return None

    stack = [root]

    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root

if __name__ == '__main__':

    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    # Invert
    invert_binary_tree(root)


    # Simple print function to verify
    def print_tree(node):
        if not node:
            return
        print(node.value)
        print_tree(node.left)
        print_tree(node.right)


    print_tree(root)






