class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binary_tree_diameter(root):
    if not root:
        return 0

    stack = [(root, False)]
    heights = {}
    diameter = 0

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if visited:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)

            diameter = max(diameter, left_height + right_height)
            heights[node] = 1 + max(left_height, right_height)

        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return diameter



# def binaryTreeDiameter(tree):
#     def dfs(node):
#         if node is None:
#             return (0, 0)  # (height, diameter)
#
#         left_height, left_diameter = dfs(node.left)
#         right_height, right_diameter = dfs(node.right)
#
#         # Height of current node
#         current_height = 1 + max(left_height, right_height)
#
#         # Diameter passing through this node
#         diameter_through_node = left_height + right_height
#
#         # Best diameter so far
#         current_diameter = max(
#             diameter_through_node,
#             left_diameter,
#             right_diameter
#         )
#
#         return (current_height, current_diameter)


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.right.left = BinaryTree(5)
    root.left.right.right = BinaryTree(6)

    print(binary_tree_diameter(root))  # Output: 3