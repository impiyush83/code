class Trie:
    def __init__(self):
        self.next = dict()
        self.eow = False

def insert(root, word):
    word_len = len(word)
    for i in range(len(word)):
        if not root.next.get(word[i]):
            root.next[word[i]] = Trie()
        root = root.next[word[i]]
        if word_len - 1 == i:
            root.eow = True



words = list(map(str, input().split()))
trie = Trie()

for i, word in enumerate(words):
    temp = trie
    for character in word:
        insert(trie, word)

import pdb
pdb.set_trace()

