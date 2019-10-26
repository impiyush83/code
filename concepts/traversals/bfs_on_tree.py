class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def bfs(root: Node) -> None:
    queue = [root]
    while queue:
        data = queue.pop(0)
        print(data.val)
        if data.left:
            queue.append(data.left)
        if data.right:
            queue.append(data.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

bfs(root)
