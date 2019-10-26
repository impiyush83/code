t = int(input())
while t:
    n, m, q = list(map(int, input().split()))

    matrix = []
    for i in range(0, n):
        temp = []
        for j in range(0, m):
            temp.append(0)
        matrix.append(temp)
    row = dict()
    col = dict()
    while q:
        a1, a2 = list(map(int, input().split()))
        a1 = a1 - 1
        a2 = a2 - 1

        if not row[a1]:
            row[a1] = 1
        else:
            row[a1] += 1

        if not row[a2]:
            col[a2] = 1
        else:
            col[a2] += 1
        q -= 1

    odders = 0
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] % 2 == 1:
                odders += 1
    print(odders)
    t -= 1
