import random

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# define class binary tree
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        self.insert_by_node(self.root, data)
        return

    def insert_by_node(self, node, data):
        # pdb.set_trace()
        if data <= node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self.insert_by_node(node.left, data)
                return
        # fill new code
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self.insert_by_node(node.right, data)
                return


    def contains(self, data):
        return self.contains_by_node(self.root, data)

    def contains_by_node(self, node, data):
        '''
        fill in the code
        '''
        if node:
            if node.data == data:
                return True
            if data <= node.data:
                return self.contains_by_node(node.left, data)
            else:
                return self.contains_by_node(node.right, data)
        return False

def in_order(node):
    if node:
        in_order(node.left)
        print("{}, ".format(node.data))
        in_order(node.right)


def in_order_traversal(T):
    in_order(T.root)

def preorder(node):
    if node:
        print("{}, ".format(node.data))
        in_order(node.left)
        in_order(node.right)


def preorder_traversal(T):
    preorder(T.root)


random.seed(10)
dataset = [random.randint(0, 100)for x in range(15)]
queryset = [0, 20, 13, 62, 15]

tree = BinaryTree(dataset[0])
print(dataset)
for i in range(1, len(dataset)):
    tree.insert(dataset[i])

# in_order_traversal(tree)
preorder_traversal(tree)
'''
fill in the code
query elements in queryset, print results
'''

for i in queryset:
    if tree.contains(i):
        print("Item contains in dataset", i)
    else:
        print("Item does not contains in dataset", i)
