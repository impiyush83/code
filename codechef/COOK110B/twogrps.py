def findSplitPoint(arr, n):
    leftSum = 0
    for i in range(0, n):
        leftSum += arr[i]

    rightSum = 0
    for i in range(n - 1, -1, -1):

        rightSum += arr[i]

        leftSum -= arr[i]

        if rightSum == leftSum:
            return i

    return -1


def printTwoParts(arr, n):
    splitPoint = findSplitPoint(arr, n)

    if splitPoint == -1 or splitPoint == n:
        return 0

    for i in range(0, n):
        if splitPoint == i:
            pass
        return arr[i]


t = int(input())
while t:
    a, b, c = list(map(int, input().split()))
    if a + b == 0:
        if 0 == c % 2:
            print("YES")
            t -= 1
            continue
        else:
            print("NO")
            t -= 1
            continue

    if c + b == 0:
        if 0 == a % 2:
            print("YES")
            t -= 1
            continue
        else:
            print("NO")
            t -= 1
            continue

    if a + c == 0:
        if 0 == b % 2:
            print("YES")
            t -= 1
            continue
        else:
            print("NO")
            t -= 1
            continue

    if (a * 1 + b * 2 + c * 3) % 2 == 1:
        print("NO")
        t -= 1
        continue
    else:
        print("YES")
        t -= 1
        continue
