t = int(input())
while t:
    n = int(input())
    p = list(map(int, input().split()))
    good_price_cnt = 1
    for i in range(1, n):
        if i > 4:
            if p[i] < min(p[i - 5:i]):
                good_price_cnt += 1
                # print(p[i - 5:i], good_price_cnt)
        else:
            if p[i] < min(p[0:i]):
                good_price_cnt += 1
                # print(p[0:i], good_price_cnt)
    print(good_price_cnt)
    t -= 1
