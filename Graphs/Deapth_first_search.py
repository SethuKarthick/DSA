

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        child = Node(name)
        self.children.append(child)

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array


root = Node("A")
root.add_child("B")
root.add_child("C")
root.add_child("D")   # adds B, C, D

# Add children to C and D
root.children[1].add_child("E")   # C -> E
root.children[2].add_child("F")   # D -> F

result = root.depth_first_search([])
print(result)