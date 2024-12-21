class Searching:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start_node):
        visited = []
        queue = []

        visited.append(start_node)
        queue.append(start_node)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def dfs(self, start_node):
        visited = set()
        stack = []

        visited.add(start_node)
        stack.append(start_node)

        while stack:
            s = stack.pop()
            print(s, end=' ')

            for n in reversed(self.graph[s]):
                if n not in visited:
                    visited.add(n)
                    stack.append(n)

graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

search_instance = Searching(graph)

print("BFS:")
search_instance.bfs('A')

print("\nDFS:")
search_instance.dfs('A')
