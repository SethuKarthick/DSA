matrix = [
  [ 0, -1, -3,  2],
  [ 1, -2, -5, -1],
  [ 3,  0, -1, -2]
]

from collections import deque

def minimum_passes(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    passes = 0
    queue = deque()

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] > 0:
                queue.append((row, col))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        flips = False

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] < 0:
                    matrix[nx][ny] *= -1
                    flips = True
                    queue.append((nx, ny))


        if flips:
            passes += 1

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] < 0:
                return -1
    return passes


res = minimum_passes(matrix)
print(res)
