for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_rev = list(reversed(a))
    if a == a_rev and set(a) == set(range(1, 8)):
        print("yes")
    else:
        print("no")
