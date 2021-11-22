import string

class TrieNode:
    def __init__(self, s):
        self.is_leaf = False
        self.children = dict()
        self.str = s

def insert(key, head):
    node = head
    for character in key:
        if not node.children.get(character):
            node.children[character] = TrieNode(node.str + character)
        node = node.children[character]
    node.is_leaf = True

def countChildren(node):
    count = 0
    for i in string.ascii_letters:
        if not node.children.get(i):
            continue
        count += 1
    return count

def trie_words(trie):
    if trie:
        if trie.is_leaf:
            yield trie.str
        for k, v in trie.children.items():
            yield from trie_words(trie.children[k])
    return None

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

def remove(s1, node, level=0):
    if not node:
        return None

    if level == len(s1):
        if node.is_leaf:
            node.is_leaf = False

        if len(node.children) == 0:
            node = None

        return node

    node.children[s1[level]] = remove(s1, node.children[s1[level]], level + 1)
    if len(node.children) == 0 and not node.is_leaf:
        node = None
    return node


# Driver code to test the code
D = "aAacabcabc"
P = "aAad"

root = TrieNode("")
insert(D, root)
insert(P, root)

# removing D string
remove(D, root, 0)

x = trie_words(root)
for i in x:
    print(i)
