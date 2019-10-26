class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder(root: Node) -> None:
    if root:
        print(root.val, end=', '),
        preorder(root.left)
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder(root)
