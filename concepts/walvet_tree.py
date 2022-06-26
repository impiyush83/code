from collections import  defaultdict

class WaveletTree:
    def __init__(self):
        self.list = []
        self.rank = []
        self.left = None
        self.right = None

    def assign_ranks(self):
        if not self.list:
            return []
        maxi = max(self.list)
        mini = min(self.list)
        mid = (maxi + mini) / 2
        return [0 if item <= mid else 1 for item in self.list]

def create_walvet_tree(_list):
    _root = WaveletTree()
    _root.list = _list
    if len(_list) <= 1:
        return _root

    _root.rank = _root.assign_ranks()

    right = []
    left = []

    for index in range(0, len(_root.rank)):
        if _root.rank[index] == 1:
            right.append(_root.list[index])
        else:
            left.append(_root.list[index])

    _root.left = create_walvet_tree(left)
    _root.right = create_walvet_tree(right)
    return _root


def inorder(_root):
    if _root:
        print(_root.list, _root.rank, _root.left, _root.right)
        inorder(_root.left)
        inorder(_root.right)


def level_order(_root):

    if not _root:
        print("Empty tree")
        return

    dicto = defaultdict(lambda : [])

    queue = [(_root, 0)]

    while queue:
        item, lvl = queue.pop(0)
        if item == 'X':
            continue
        dicto[lvl].append(
            "".join([str(item) for item in item.rank]) if item.rank else 'X'
        )
        queue.append((item.left if item.left else 'X', lvl + 1))
        queue.append((item.right if item.left else 'X', lvl + 1))
    return dicto


def rqq(ksmallest, left, right):

    pass


print("Enter input list:")
# input_list = list(set(map(int, input().split())))
input_list = [6 , 2, 0 ,7 , 9, 3, 1 , 8 , 5, 4]
root = create_walvet_tree(input_list)
inorder(root)
dicto = level_order(root)
print(dicto)
# print("RQQ inputs:")
# k, l, r = list(map(int, input().split()))
# rqq(k, l, r)




