for _ in range(int(input())):
    l = int(input())
    ll = list(map(int, input().split()))
    mini = min(ll)
    ans = 0
    for i in ll:
        ans += (i-mini)
    print(ans)