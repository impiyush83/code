from operator import itemgetter
from math import sqrt


def binarySearchUpper(l, r, x):
    if l <= r:
        mid = (l + r) / 2
        if arr[mid][0] == x:
            return binarySearchUpper(l, mid - 1, x)
        elif arr[mid][0] < x:
            return binarySearchUpper(mid + 1, r, x)
        else:
            return binarySearchUpper(l, mid - 1, x)
    else:
        return l


def binarySearchLower(l, r, x):
    if l <= r:
        mid = (l + r) / 2
        if arr[mid][0] == x:
            return binarySearchLower(mid + 1, r, x)
        elif arr[mid][0] < x:
            return binarySearchLower(mid + 1, r, x)
        else:
            return binarySearchLower(l, mid - 1, x)
    else:
        return r


def preprocess(n, blk_sz, blk_id):
    for i in range(n):
        new_arr.append(arr[i][1])
        if i % blk_sz == 0:
            blk_id += 1
        blocks[blk_id] = max(arr[i][1], blocks[blk_id])


def query(l, r, blk_sz):
    maxi = 0
    while l < r and l % blk_sz != 0 and l != 0:
        maxi = max(maxi, new_arr[l])
        l += 1
    while l + blk_sz <= r:
        maxi = max(maxi, blocks[l / blk_sz])
        l += 1
    while l <= r:
        maxi = max(maxi, new_arr[l])
        l += 1
    return maxi


n = int(input())
arr = []
for i in range(n):
    arr.append(map(int, input().split()))
arr.sort(key=itemgetter(0))

blocks = [0 for i in range(10 ** 3 + 1)]
new_arr = []
blk_id = -1
blk_sz = int(sqrt(n))
preprocess(n, blk_sz, blk_id)

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    a = binarySearchUpper(0, n - 1, a)
    b = binarySearchLower(0, n - 1, b)

    print(query(a, b, blk_sz))
