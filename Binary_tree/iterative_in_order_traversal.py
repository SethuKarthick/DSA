from typing import Optional, List

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#
#
# def iterative_in_order_traversal(root):
#     result = []
#     def traversal(node):
#         if node.left:
#             traversal(node.left)
#         result.append(node.value)
#         if node.right:
#             traversal(node.right)
#
#     if root:
#         traversal(root)
#     return result
#
#

def inorderTraversal(root: Optional[BinaryTree]) -> List[int]:
    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result





if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    # Perform iterative in-order traversal
    result = inorderTraversal(root)
    print(result)  # Expected output: [4, 2, 5, 1, 3]
