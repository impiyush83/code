t = int(input())
while t:
    n, k = list(map(int, input().split()))
    ll = list(map(int, input().split()))
    cnt = 0
    for i in range(0, len(ll)):
        if (ll[i] + k) % 7 == 0:
            cnt += 1
    print(cnt)
    t -= 1
