from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def find_node_distance_from_k(root, target, k):
    if not root:
        return []
    parents_dict = {}

    def dfs(node, parent = None):
        if not node:
            return

        parents_dict[node] = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root)

    queue = deque([(target, 0)])
    visited = set([target])
    result = []

    while queue:
        node, dis = queue.popleft()

        if dis == k:
            result.append(node.value)
            continue

        for neighbor in (node.left, node.right, parents_dict[node]):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dis + 1))


    return result

if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(4)
    root.right.right = BinaryTree(5)

    target = root.right  # node with value 3
    k = 1

    print(find_node_distance_from_k(root, target, k))
