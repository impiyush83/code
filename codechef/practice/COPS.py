for _ in range(int(input())):
    M, x, y = list(map(int, input().split()))
    cops = list(map(int, input().split()))
    max_area = x * y
    houses = []
    for i in range(0, 100):
        houses.append(1)
    for cop in cops:
        cop = cop - 1
        lower_bound = cop - max_area if (cop - max_area) > 0 else 0
        upper_bound = cop + max_area if (cop+max_area) < 100 else 99
        for i in range(lower_bound, upper_bound + 1):
            houses[i] = 0
    cnt = 0
    for i in houses:
        if i == 1:
            cnt += 1
    print(cnt)
