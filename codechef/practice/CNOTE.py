for _ in range(int(input())):
    x, y, k, n = list(map(int, input().split()))
    req = x - y
    pages_costs = []
    while n:
        pi, ci = list(map(int, input().split()))
        pages_costs.append([pi, ci])
        n -= 1
    flag = 0
    for page_cost in pages_costs:
        if req <= page_cost[0] and  page_cost[1] <= k:
            flag = 1
            break
    if flag:
        print("LuckyChef")
    else:
        print("UnluckyChef")
