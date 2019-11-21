class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root: TreeNode, l: int, h: int):
        if root is None:  # assumed that empty tree is a valid BST
            return True

        if root.val <= l or root.val >= h:
            return False

        return self.helper(root.left, l, root.val) and self.helper(root.right,
                                                                   root.val, h)