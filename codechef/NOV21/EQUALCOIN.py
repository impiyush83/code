
t = int(input())
while t:
    n = list(map(int, input().split()))
    if n[0] % 2 == 0:
        if n[0] == 0 and n[1] % 2 == 1:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
    t -= 1