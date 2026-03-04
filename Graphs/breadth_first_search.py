class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))


    def breadth_first_search(self, array):
        queue = [self]

        while len(queue) > 0:
            current_node = queue.pop(0)
            array.append(current_node.name)
            for child in current_node.children:
                queue.append(child)
        return array


root = Node("A")

# Add children
root.add_child("B")
root.add_child("C")
root.add_child("D")

# Add grandchildren
root.children[1].add_child("E")  # C -> E
root.children[2].add_child("F")  # D -> F

result = root.breadth_first_search([])
print(result)





