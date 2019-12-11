class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node == None:
                return None

            temp = node

            left = helper(node.left)
            right = helper(node.right)

            node.right = left
            node.left = right

            return node

        helper(root)
        return root
