from sys import maxsize

INT_MAX = int(maxsize)
INT_MIN = -INT_MAX

for _ in range(int(input())):
    g, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    max_dp = [INT_MIN]
    max_until_now = INT_MIN
    for i in range(len(A)):
        if max_until_now < A[i]:
            max_until_now=A[i]
        max_dp.append(max_until_now)
    for index in Q:
        print(max_dp[index])
