def binarysearch(arr, low, high, key):
    if low < high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            return binarysearch(arr, mid + 1, high, key)
        else:
            return binarysearch(arr, low, mid - 1, key)
    return False

def solution(a, b, c, t):
    a.sort()
    b.sort()
    c.sort()
    for i in a:
        for j in b:
            to_find = t - (i + j)
            print(to_find)
            if binarysearch(c, 0, len(c), to_find):
                return i, j, to_find
    return False


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
t = int(input())
print(solution(a, b, c, t))

