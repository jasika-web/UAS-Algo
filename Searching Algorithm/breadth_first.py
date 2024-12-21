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

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

search_instance = Searching(graph)

search_instance.bfs('A')