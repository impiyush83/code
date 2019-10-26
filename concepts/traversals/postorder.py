class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def postorder(root: Node) -> None:
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=', '),


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postorder(root)
