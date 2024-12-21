from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, x, y, visited):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0 and not visited[x][y]

    def lee_algorithm(self, start, end):
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        distance = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]

        queue = deque([start])
        visited[start[0]][start[1]] = True
        distance[start[0]][start[1]] = 0

        while queue:
            x, y = queue.popleft()

            if (x, y) == end:
                return distance[x][y]

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny, visited):
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

        return -1


# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

graph = Graph(grid)
result = graph.lee_algorithm(start, end)
print("Shortest Path Length:", result)