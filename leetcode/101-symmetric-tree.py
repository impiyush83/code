class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left,right):
            if not left and not right:
                return True
            if not right or not left:
                return False
            if left.val!=right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        if not root:
            return True
        return helper(root.left, root.right)
