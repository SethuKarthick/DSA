class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flatten_binary_tree(root):
    left_head, _ = flatten_tree(root)
    return left_head

def flatten_tree(node):
    if not node:
        return None, None


    if node.left:
        left_head, left_tail = flatten_tree(node.left)
        connect_nodes(left_tail, node)
    else:
        left_head = node
        left_tail = None

    if node.right:
        right_head, right_tail = flatten_tree(node.right)
        connect_nodes(node, right_head)
    else:
        right_head = None
        right_tail = node


    return left_head, right_tail

def connect_nodes(left, right):
    if left and right:
        left.right = right
        right.left = left


def print_flattened_tree(root):
    # Print the flattened tree in the right direction (head to tail)
    current = root
    print("Flattened Tree (head to tail): ", end="")
    while current:
        print(current.value, end=" <-> " if current.right else " <-> None")
        current = current.right
    print()  # To ensure we move to the next line after printing the list



if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(5)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(4)
    root.right.right = BinaryTree(6)

    new_head = flatten_binary_tree(root)
    print_flattened_tree(new_head)
#
#
# # 6 <-> 5 <-> 1 <-> 4 <-> 2 <-> 3 <-> None
#
# # 3 <-> 2 <-> 4 <-> 1 <-> 5 <-> 6 <-> None
#



