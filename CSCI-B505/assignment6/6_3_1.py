"""
Insertion of 2 string D and P takes D + P time = O(D + P)
Traversing till there are more than 1 node, takes O(N) time.
"""

ALPHABET_SIZE = 26
indexes = 0

class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.children = [None]*ALPHABET_SIZE


def insert(key, root):
    node = root
    for level in range(len(key)):
        index = ord(key[level]) - ord('a')
        if node.children[index] == None:
            node.children[index] = TrieNode()
        node = node.children[index]
    node.is_leaf = True

def buildTrie(D, P, root):
    """
    Builds trie
    :param D: string
    :param P:  string
    :return: None
    """
    insert(D, root)
    insert(P, root)

# Counts and returns number of children of the node
def countChildren(node):
    count = 0
    for i in range(ALPHABET_SIZE):
        if node.children[i] != None:
            count +=1
            # Keeping track of diversion in the trie
            global indexes
            indexes = i
    return count

# Traverse on trie and return longest common prefix 
def traverse(root):
    head = root
    prefix = ""
    while(countChildren(head) == 1 and head.is_leaf == False):
        head = head.children[indexes]
        prefix += chr(97 + indexes)
    return prefix or -1

def longestCommonPrefix(D, P, root):
    buildTrie(D, P, root)
    return traverse(root)

# Driver code to test the code
D = "aacabcabc"
P = "abc"
root = TrieNode()
print(longestCommonPrefix(D, P, root))
