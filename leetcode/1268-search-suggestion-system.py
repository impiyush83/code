from typing import List

class TrieNode:
    def __init__(self):
        self.node = dict()
        self.word = ""
        self.e = False
        self.priority = 0


def insert(root, string, cnt):
    for i in string:
        if root.node.get(i):
            root = root.node[i]
        else:
            parent = root.word
            root.node[i] = TrieNode()
            root = root.node[i]
            root.word = parent + i
    root.priority = cnt
    root.e = True


def fetch_leaf_nodes(root):
    queue = []
    seto = set()
    if root and root.e:
        seto.add((root.word, root.priority))
    for i in root.node.keys():
        queue.append(root.node[i])
    while queue:
        item = queue.pop(0)
        if len(item.node.keys()) == 0:
            seto.add((item.word, item.priority))
        else:
            if item.e:
                seto.add((item.word, item.priority))
            for j in item.node.keys():
                queue.append(item.node[j])
    return list(seto)


def suggested_words(searched_word, root):
    for i in searched_word:
        if root.node.get(i):
            root = root.node[i]
        else:
            return [""]
    return fetch_leaf_nodes(root)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> \
            List[List[str]]:
        trie = TrieNode()
        print(sorted(products))
        cnt = 0
        for word in sorted(products):
            insert(trie, word, cnt)
            cnt += 1

        ans = []

        for i in range(1, len(searchWord) + 1):
            searched_word = searchWord[0:i]
            print(searched_word)
            ans.append(suggested_words(searched_word, trie))

        final = []
        for i in ans:
            if i[0]:
                final.append([j[0] for j in sorted(i, key=lambda i: i[1])[:3]])
            else:
                final.append([])
        return final


