A = [[2], [1]]  # r = 2 = x , (c = 1) =  y
B = [[2, 1]]  # (r = 1) = y , c = 2 = z

x = 2
z = 2
y = 1

C = []
for i in range(0, x):
    l = []
    for j in range(0, z):
        l.append(0)
    C.append(l)
print(C)
for i in range(0, x):
    for j in range(0, z):
        C[i][j] = 0
        for k in range(0, y):
            C[i][j] += A[i][k] + B[k][j]
print(C)