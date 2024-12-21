import heapq


class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


class Basic:
    def __init__(self, chars, freq):
        self.chars = chars
        self.freq = freq
        self.huffman_codes = {}

    def build_huffman_tree(self):
        # Create a priority queue of nodes
        priority_queue = [Node(char, f)
                          for char, f in zip(self.chars, self.freq)]
        heapq.heapify(priority_queue)

        # Build the Huffman tree
        while len(priority_queue) > 1:
            left_child = heapq.heappop(priority_queue)
            right_child = heapq.heappop(priority_queue)
            merged_node = Node(
                frequency=left_child.frequency + right_child.frequency)
            merged_node.left = left_child
            merged_node.right = right_child
            heapq.heappush(priority_queue, merged_node)

        return priority_queue[0]

    def generate_huffman_codes(self, node, code=""):
        if node is not None:
            if node.symbol is not None:
                self.huffman_codes[node.symbol] = code
            self.generate_huffman_codes(node.left, code + "0")
            self.generate_huffman_codes(node.right, code + "1")

    def encode(self):
        # Build the Huffman tree
        root = self.build_huffman_tree()
        # Generate Huffman codes
        self.generate_huffman_codes(root)
        return self.huffman_codes


# Usage example
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [4, 7, 15, 17, 22, 42]

basic = Basic(chars, freq)
huffman_codes = basic.encode()

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")
