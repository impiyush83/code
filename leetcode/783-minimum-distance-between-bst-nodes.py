import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        listo = list(inorder(root))
        mini = sys.maxsize
        for i in range(0,len(listo)-1):
            if mini > listo[i+1] - listo[i]:
                mini = listo[i+1] - listo[i]
        return mini