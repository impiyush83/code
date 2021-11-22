"""
Insertion of 2 string D and P takes D + P time = O(D + P)
Traversing till there are more than 1 node, takes O(N) time.
"""

import string

class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.children = dict()

def insert(key, head):
    node = head
    for character in key:
        if not node.children.get(character):
            node.children[character] = TrieNode()
        node = node.children[character]
    node.is_leaf = True

def countChildren(node):
    count = 0
    for i in string.ascii_letters:
        if not node.children.get(i):
            continue
        count += 1
    return count

# takes linear time
def longestCommonPrefix(node):
    head = node
    prefix = ""
    while countChildren(head) == 1 and not head.is_leaf:
        # this take O(1) as it has only 1 children
        for k, v in head.children.items():
            prefix += k
            head = v
    return prefix or -1


# Driver code to test the code
D = "aAacabcabc"
P = "aAa"

root = TrieNode()
insert(D, root)
insert(P, root)
print(longestCommonPrefix(root))
