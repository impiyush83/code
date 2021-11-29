import random


class DirectedGraph:
    def __init__(self, n):
        self.num_nodes = n
        self.nodes = [[] for i in range(n)]

    # edge node1 -> node2 (directed)
    def insert(self, node1, node2):
        self.nodes[node1].append(node2)

    def deleteConnection(self, node):
        self.nodes[node].clear()


def dfs(graph, starting_node):
    visited = [False for i in range(graph.num_nodes)]

    # Key function call
    dfs_recursive(graph, starting_node, visited)

    # The following lines are for demonstrating results
    print("Starting from node {:d}, we visited {:d} nodes".format(starting_node,
                                                              sum(visited)))
    visited_nodes = []
    for i in range(len(visited)):
        if visited[i]:
            visited_nodes.append(i)
    print("The following nodes were visited: ")
    print(visited_nodes)


def dfs_recursive(graph, starting_node, visited):
    '''
    fill in code here
    '''
    if visited[starting_node]:
        return

    visited[starting_node] = True
    print(starting_node)
    for node in graph.nodes[starting_node]:
        dfs_recursive(graph, node, visited)
    return


random.seed(100)
num_nodes = 20

graph = DirectedGraph(num_nodes)

ignore_list = [5, 10, 15]


for i in range(num_nodes):
    while len(graph.nodes[i]) < 3:
        node = random.randint(0, num_nodes-1)
        if node != i and (node not in graph.nodes[i]) and (node not in ignore_list):
            graph.insert(i, node)

graph.deleteConnection(5)
graph.deleteConnection(10)
graph.deleteConnection(15)

graph.insert(5, 10)
graph.insert(5, 15)
graph.insert(15, 10)

print(graph.nodes)

dfs(graph, 0)
dfs(graph, 5)