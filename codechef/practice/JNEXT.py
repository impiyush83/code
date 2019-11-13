for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    flag = 0
    d1 = -99999999
    d2 = -99999999
    for i in range(len(ll) - 1, 1, -1):
        if ll[i] > ll[i - 1]:
            print(ll[i], ll[i - 1])
            flag = 1
            d1 = i - 1
            break
    if flag:
        mini = 999999
        # print(d1)
        for i in range(d1 + 1, len(ll)):
            # print(ll[i], ll[d1])
            x = ll[i] - ll[d1]
            if x > 0:
                if mini > x:
                    mini = x
                    d2 = i
        print(d1, d2)
        ll[d1], ll[d2] = ll[d2], ll[d1]
        ans = []
        ans.extend(ll[0:d1 + 1])
        ans.extend(sorted(ll[d1 + 1:]))
        string = ""
        for i in ans:
            string += str(i)
        print(int(string))
    else:
        print(None)
