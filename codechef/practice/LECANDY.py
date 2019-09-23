t = int(input())
while t:
    n, c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) > c:
        print("No")
    else:
        print("Yes")
    t -= 1
