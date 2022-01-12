class TrieNode:
    def __init__(self):
        self.node = dict()
        self.word = ""
        self.e = False
        self.priority = 0


def insert(root, string, cnt):
    for i in range(len(string)):
        if root.node.get(string[i]):
            root = root.node[string[i]]
        else:
            parent = root.word
            root.node[string[i]] = TrieNode()
            root = root.node[string[i]]
            root.word = parent + string[i]
            if i == len(string) - 1:
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
    return seto

def suggested_words(searched_word, root):

    for i in searched_word:
        if root.node.get(i):
            root = root.node[i]
        else:
            return [""]
    return fetch_leaf_nodes(root)

products = ["mobile","mouse","moneypot","monitor","mousepad"]
search_word = "mouse"
trie = TrieNode()
cnt = 0
for word in sorted(products):
    insert(trie, word, cnt)
    cnt += 1

ans = []

for i in range(1, len(search_word) + 1):
    searched_word = search_word[0:i]
    print(searched_word)
    ans.append(suggested_words(searched_word, trie))

