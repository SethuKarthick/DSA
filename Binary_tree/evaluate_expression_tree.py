

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression_tree(tree):
    if tree.left is None and tree.right is None:
        return tree.value

    left_value = evaluate_expression_tree(tree.left)
    right_value = evaluate_expression_tree(tree.right)

    if tree.value == -1:
        return left_value + right_value
    elif tree.value == -2:
        return left_value - right_value
    elif tree.value == -3:
        return int(left_value / right_value)
    else:
        return left_value * right_value


if __name__ == '__main__':
    root = BinaryTree(-1)
    root.left = BinaryTree(-2)
    root.right = BinaryTree(-3)

    root.left.left = BinaryTree(2)
    root.left.right = BinaryTree(3)

    root.right.left = BinaryTree(4)
    root.right.right = BinaryTree(5)

    print(evaluate_expression_tree(root))

