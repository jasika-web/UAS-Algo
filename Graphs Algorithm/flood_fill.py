class Graphs:
    def __init__(self, img):
        self.img = img

    def dfs(self, x, y, prev_clr, new_clr):
        # Base case: if the current pixel is not 
        # the same as the previous color
        if self.img[x][y] != prev_clr:
            return

        # Marking it as the new color
        self.img[x][y] = new_clr

        # Moving up, right, down, and left one by one
        n = len(self.img)
        m = len(self.img[0])
        if x - 1 >= 0:
            self.dfs(x - 1, y, prev_clr, new_clr)
        if y + 1 < m:
            self.dfs(x, y + 1, prev_clr, new_clr)
        if x + 1 < n:
            self.dfs(x + 1, y, prev_clr, new_clr)
        if y - 1 >= 0:
            self.dfs(x, y - 1, prev_clr, new_clr)

    def flood_fill(self, x, y, new_clr):
        prev_clr = self.img[x][y]
        if prev_clr == new_clr:
            return
        self.dfs(x, y, prev_clr, new_clr)

if __name__ == "__main__":
    img = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    # Co-ordinate provided by the user
    x = 1
    y = 1

    # New color that has to be filled
    new_clr = 3

    graph_instance = Graphs(img)
    graph_instance.flood_fill(x, y, new_clr)

    # Printing the updated img
    for row in graph_instance.img:
        print(' '.join(map(str, row)))