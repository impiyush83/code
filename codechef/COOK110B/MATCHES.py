matches = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

t = int(input())
while t:
    a, b = list(map(str, input().split()))
    # print(a, b)
    c = str(int(a) + int(b))
    ans = 0
    for digit in c:
        ans += matches[digit]
    print(ans)
    t -= 1
