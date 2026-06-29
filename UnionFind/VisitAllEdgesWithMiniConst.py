"""
    Context: Amazon is expanding its delivery network.
    You are given n delivery stations, and a list of possible roads that can be built between them,
    each with an associated construction cost. Your task is to connect all delivery stations
    with the minimum total cost, so that packages can be routed between any two stations.

    Problem Statement:
    Given n stations (labeled 1 to n) and a list of edges where edges[i] = [station1, station2, cost],
    return the minimum cost to connect all stations.

    If it is not possible to connect all stations, return -1.

    Example:
    Input:
    n = 4
    edges = [[1,2,3],[1,3,5],[2,3,1],[3,4,4]]

    Output: 8

    Explanation:
    Connect 2-3 (cost 1), 1-2 (cost 3), 3-4 (cost 4) → Total = 8
"""

n = 4
edges = [[1,2,3],[1,3,5],[2,3,1],[3,4,4]]



class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def find_min_cost(edges , n):
    edges.sort(key=lambda x : x[2])
    uf = UnionFind(n)

    total_cost = 0
    visited_edges = []

    for u, v, cost in edges:
        if uf.union(u, v):
            total_cost += cost
            visited_edges.append((u, v))
    return total_cost, visited_edges


res, visited_edges = find_min_cost(edges, n)
print(res)
print(visited_edges)


def longest_streak(data, m):
    max_streak = 0
    current_streak = 0

    lst = ["Y"] * m
    expected_res = "".join(lst)

    for day in data:
        # check if all microservices are working
        if day == expected_res:
            current_streak += 1
            continue
        max_streak = max(max_streak, current_streak)
        current_streak = 0

    return max_streak