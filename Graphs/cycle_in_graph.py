WHITE, GREY, BLACK = 1, 2, 3

def cycle_in_graph(edges):
    number_of_edges = len(edges)
    colors = [WHITE for _ in range(number_of_edges)]

    for node in range(number_of_edges):

        if colors[node] != WHITE:
            continue

        contains_cycle = traverse_and_color_nodes(edges, node, colors)
        if contains_cycle:
            return True

    return False

def traverse_and_color_nodes(edges, node, colors):
    colors[node] = GREY

    neighbours = edges[node]

    for neighbour in neighbours:
        neighbour_color = colors[neighbour]

        if neighbour_color == GREY:
            return True

        if neighbour_color != WHITE:
            continue

        contains_cycle = traverse_and_color_nodes(edges, neighbour, colors)
        if contains_cycle:
            return True

    colors[node] = BLACK
    return False


graph1 = {
    0: [1],
    1: [2],
    2: [0]
}

graph2 = {
    0: [1],
    1: [2],
    2: []
}

print(cycle_in_graph(graph1))  # True
print(cycle_in_graph(graph2))