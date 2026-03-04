src = [0, 0]
dst = [10, 10]

from collections import deque

def knight_connection(src, dst):

    x1, y1 = src
    x2, y2 = dst

    if (x1, y1) == (x2, y2):
        return 0

    # start =  (abs(x1-x2), abs(y1- y2))

    moves = [
        (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    queue = deque()
    queue.append(((x1, y1), 0))
    visited = set()
    visited.add((x1, y1))

    while queue:
        (current_x, current_y), steps = queue.popleft()

        if current_x == x2 and current_y == y2:
            return steps

        for dx, dy in moves:
            nx, ny = current_x + dx, current_y + dy
            if (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))
#



# from collections import deque
#
# def knight_connection(src, dst):
#     x1, y1 = src
#     x2, y2 = dst
#
#     # Already at target
#     if (x1, y1) == (x2, y2):
#         return 0
#
#     # Compute relative position
#     start = (0, 0)
#     target = (x2 - x1, y2 - y1)
#
#     # BFS moves
#     moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
#
#     queue = deque([(start, 0)])
#     visited = set([start])
#
#     while queue:
#         (cx, cy), steps = queue.popleft()
#
#         if (cx, cy) == target:
#             return steps
#
#         for dx, dy in moves:
#             nx, ny = cx + dx, cy + dy
#             new_pos = (nx, ny)
#             if new_pos not in visited:
#                 visited.add(new_pos)
#                 queue.append(((nx, ny), steps + 1))




res = knight_connection(src, dst)
print(res)