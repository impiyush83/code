
# cook your dish here

t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))

    odd_counter = 0

    for i in a:
        if i % 2 == 1:
            odd_counter += 1
    print(odd_counter // 2)
    t -= 1