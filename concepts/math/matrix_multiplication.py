A = [[2], [1]]  # r = 2 = x , (c = 1) =  y
B = [[2, 1]]  # (r = 1) = y , c = 2 = z



C = []
for i in range(0, len(A)):
    l = []
    for j in range(0, len(B[0])):
        l.append(0)
    C.append(l)
print(C)

for i in range(0, len(A)):
    for j in range(0, len(B[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]
print(C)