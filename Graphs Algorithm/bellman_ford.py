class Graphs:
    def __init__(self, graph):
        self.graph = graph

    def bellman_ford(self, source):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[source] = 0

        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, weight in self.graph[u].items():
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        for u in self.graph:
            for v, weight in self.graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains negative weight cycle")

        return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }
    source = 'A'

    graph_instance = Graphs(graph)
    shortest_distances = graph_instance.bellman_ford(source)
    print(shortest_distances)