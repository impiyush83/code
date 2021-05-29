from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        return list(inorder(root))



class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(node, output):
            if node:
                inorder(node.left, output)
                output.append(node.val)
                inorder(node.right, output)

        output = list()
        inorder(root, output)
        return output

solution1 = Solution1()
a = TreeNode(1)
a.left = TreeNode(3)
a.right = TreeNode(4)
print(solution1.inorderTraversal(a))