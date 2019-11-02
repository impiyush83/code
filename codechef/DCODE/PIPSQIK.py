t = int(input())
while t:
    n, h, y1, y2, life = list(map(int, input().split()))
    bcr = 0
    for i in range(1, n + 1):
        type_b, X = list(map(int, input().split()))
        if type_b == 1:
            if h - y1 > X:
                life -= 1
        else:
            if y2 < X:
                life -= 1
        if life ==0 :
            break
        bcr += 1
    print(bcr)
    t -= 1
