class Array:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph

    def floyd_warshall(self):
       
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph))

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        self.print_solution(dist)

    def print_solution(self, dist):

        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(self.V):
            for j in range(self.V):
                if dist[i][j] == 99999:
                    print("%7s" % ("INF"), end=" ")
                else:
                    print("%7d" % (dist[i][j]), end=' ')
            print()

if __name__ == "__main__":
    V = 4
    INF = 99999

    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]]

    # Create an instance of the Array class
    floyd_instance = Array(V, graph)

    # Perform Floyd Warshall Algorithm
    floyd_instance.floyd_warshall()

