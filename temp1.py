temp = []
n = 11
ans = [i for i in range(1,n+1)]


s = 'e'

if len(ans) <= 2:
    print(ans,)
else:
    while len(ans) > 2:
        x = []
        cnt = 0
        if s == 'e':
            for i in range(0, len(ans)):
                if i % 2 == 1 and len(ans) - cnt > 2:
                    cnt += 1
                    x.append(ans[i])
            ans = list(set(ans) - set(x))
            s = 'o'
        else:
            for i in range(0, len(ans)):
                if i % 2 == 0 and len(ans) - cnt > 2:
                    cnt += 1
                    x.append(ans[i])
            ans = list(set(ans) - set(x))
            s = 'e'
print(ans,)