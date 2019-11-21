from operator import itemgetter
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        listo = list(inorder(root))
        dicto = dict()
        for i in listo:
            if not dicto.get(i):
                dicto[i] = 1
            else:
                dicto[i] += 1
        sorted_dicto = sorted(dicto.items(), key=itemgetter(1), reverse=True)
        if not sorted_dicto:
            return []
        mode = sorted_dicto[0][1]
        ans = []
        ans.append(sorted_dicto[0][0])
        if len(sorted_dicto) > 1 :
            for i in range(1, len(sorted_dicto)):
                if sorted_dicto[i][1] == mode:
                    ans.append(sorted_dicto[i][0])
        return ans