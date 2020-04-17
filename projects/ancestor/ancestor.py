
"""
# 3 steps to graph problem:
- Describe in terms of graphs
 Nodes: individuals
 Edges: parent-child relationship

- Build our graph
 Build a graph class (write a getNeighbors function)

- Choose graph algorithm
 Traversal or search?  Traversal
 Breadth or Depth?  DFT

"""


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        child_edge = self.nodes[child]
        child_edge.add(parent)

    def get_parents(self, child):
        return self.nodes[child]


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def dft(graph, starting_node):
    stack = Stack()

    visited = set()
    visited_pairs = set()

    stack.push((starting_node, 0))

    while stack.size() > 0:
        current_pair = stack.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_parents(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                stack.push((parent, parent_distance))

    longest_distance = 0
    oldest_one = -1

    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            oldest_one = node
    return oldest_one


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()  # initiate graph

    # build graph
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

    # print(graph)

    # call dft fn
    oldest_one = dft(graph, starting_node)

    return oldest_one


relationship_list = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(relationship_list, 9))
