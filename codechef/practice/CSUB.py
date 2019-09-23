t = int(input())
while t:
    n = int(input())
    string = str(input())
    cnt = 0
    a = lambda a, b : a * b
    for i in string:
        if i == "1":
            cnt += 1
    print(int((cnt * (cnt + 1) / 2)))
    t -= 1
