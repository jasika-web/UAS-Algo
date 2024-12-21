class Basic():
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):

        if self.parent[i] == i:
            return i

        return self.find(self.parent[i])

    def unite(self, i, j):

        irep = self.find(i)

        jrep = self.find(j)

        self.parent[irep] = jrep


size = 5
uf = Basic(size)
uf.unite(1, 2)
uf.unite(3, 4)
in_same_set = (uf.find(1) == uf.find(2))
print("Are 1 and 2 in the same set?", "Yes" if in_same_set else "No")
