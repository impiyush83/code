for _ in range(int(input())):
    l1, l2 = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_length = l1 + l2 - 1
    poly = [0 for i in range(max_length)]
    print(poly)
    for i in range(0, l1):
        for j in range(0, l2):
            poly[i + j] += A[i] * B[j]
    for i in poly:
        print(i, end=" ")
