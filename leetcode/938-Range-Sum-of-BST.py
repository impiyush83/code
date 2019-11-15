class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        traversal = 0
        if root is None:
            return 0

        if L <= root.val <= R:
            traversal += root.val

        traversal += self.rangeSumBST(root.left, L, R)
        traversal += self.rangeSumBST(root.right, L, R)
        return traversal


class Solution1:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        traversal = 0
        if root:
            if L <= root.val <= R:
                traversal += root.val
            if root.left:
                traversal += self.rangeSumBST(root.left, L, R)
            if root.right:
                traversal += self.rangeSumBST(root.right, L, R)
        return traversal
