from queue import PriorityQueue


class Edge:
    def __init__(self, node1, node2, weight=1.0):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __lt__(self, other):
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority




class UnionFind:
    def __init__(self, num_nodes):
        # Initially position[i] = i
        self.position = [i for i in range(num_nodes)]

    # Return the cluster index
    def find(self, node):
        if self.position[node] == node:
            return node
        else:
            self.position[node] = self.find(self.position[node])
            return self.position[node]

    def union(self, node1, node2):
        a = self.find(node1)
        b = self.find(node2)
        # no need to union
        if a == b:
            return
        # union is needed
        else:
            if a < b:
                self.position[b] = a
            else:
                self.position[a] = b


def kruskal(edge_list, num_nodes):
    MST = []  # a list of Edge to return
    uf = UnionFind(num_nodes)
    '''
    fill in the code here

    1. Put edges in edge_list into PriorityQueue
    2. Extract each edge from PriorityQueue
        1) check if the two nodes belong to same cluster
        2) if no, do something
    '''
    pq = PriorityQueue()
    for e in edge_list:
        pq.put(e)

    while not pq.empty():
        edge = pq.get()
        node_1 = uf.find(edge.node1)
        node_2 = uf.find(edge.node2)
        if node_1 != node_2:
            MST.append(edge)
            uf.union(node_1, node_2)
    return MST


import random
# Randomly generate a graph of size 20
random.seed(100)

num_nodes = 20
edge_list = []

# For each node, add five random edges (may contain parallel edges)
node_list = []
for node1 in range(num_nodes):
    count = 0
    while count < 5:
        node2 = random.randint(0, num_nodes-1)
        if node2 not in node_list and node2 != node1:
            count += 1
            weight = random.random()   # return [0.0, 1.0]
            edge_list.append(Edge(node1, node2, weight))

for i in range(15):   # only show first 15 edges
    e = edge_list[i]
    print("{:2d}, {:2d}, {:.5f}".format(e.node1, e.node2, e.weight))


MST = kruskal(edge_list, num_nodes)

# Print size of the MST which should be num_nodes-1=19
print("The returned MST has {} edges".format(len(MST)))

total_weight = 0.0
for e in MST:
    total_weight += e.weight
    print("{:2d}, {:2d}, {:.5f}".format(e.node1, e.node2, e.weight))

print("The returned MST has total weight: {:.3f}".format(total_weight))