class TreeNode:
    def __init__(self, value):
        self.value = value
        self.ancestor = None


# Create nodes
A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")

# Set up the tree relationships (ancestor references)
A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

# Set ancestors for each node
B.ancestor = A
C.ancestor = A
D.ancestor = B
E.ancestor = B
F.ancestor = C


# Function to find the youngest common ancestor
def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
    # Calculate the depth of both descendants
    depth_one = get_descendant_depth(descendant_one, top_ancestor)
    depth_two = get_descendant_depth(descendant_two, top_ancestor)

    # Backtrack the deeper descendant to the same depth as the shallower one
    if depth_one > depth_two:
        return back_track_ancestral_tree(descendant_one, descendant_two, depth_one - depth_two)
    else:
        return back_track_ancestral_tree(descendant_two, descendant_one, depth_two - depth_one)


# Helper function to calculate depth of a descendant
def get_descendant_depth(descendant, top_ancestor):
    depth = 0
    # Ensure that the descendant exists and has an ancestor
    while descendant != top_ancestor and descendant is not None:
        depth += 1
        descendant = descendant.ancestor
    # If descendant is None, it means there's a problem in the tree structure
    if descendant is None:
        raise ValueError("One of the nodes does not have the correct ancestor.")
    return depth


# Helper function to backtrack the ancestral tree
def back_track_ancestral_tree(lowest_descendant, highest_descendant, diff):
    # Move the lower descendant up to the same depth as the higher one
    while diff > 0:
        if lowest_descendant is None:
            raise ValueError("Ancestor reference is None, check tree structure.")
        lowest_descendant = lowest_descendant.ancestor
        diff -= 1
    # Now move both descendants up until they meet at the youngest common ancestor
    while lowest_descendant != highest_descendant:
        if lowest_descendant is None or highest_descendant is None:
            raise ValueError("Ancestor reference is None, check tree structure.")
        lowest_descendant = lowest_descendant.ancestor
        highest_descendant = highest_descendant.ancestor
    return lowest_descendant


# Testing the YCA function
def test_youngest_common_ancestor():
    # Test 1: Common ancestor of D and E
    ancestor = get_youngest_common_ancestor(A, D, E)
    print(f"The YCA of D and E is: {ancestor.value}")  # Expected: B

    # Test 2: Common ancestor of D and F
    ancestor = get_youngest_common_ancestor(A, D, F)
    print(f"The YCA of D and F is: {ancestor.value}")  # Expected: A

    # Test 3: Common ancestor of E and F
    ancestor = get_youngest_common_ancestor(A, E, F)
    print(f"The YCA of E and F is: {ancestor.value}")  # Expected: A

    # Test 4: Common ancestor of D and B (should return B)
    ancestor = get_youngest_common_ancestor(A, D, B)
    print(f"The YCA of D and B is: {ancestor.value}")  # Expected: B


# Run the test
test_youngest_common_ancestor()
