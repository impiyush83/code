# cook your dish here
t = int(input())
while t:
    input_string = str(input())
    l = [0] * 26
    r = [0] * 26
    if len(input_string) == 1:
        print("YES")
        t -= 1
        continue
    mid = int(len(input_string) / 2)
    for i in range(0, mid):
        l[ord(input_string[i]) - 97] += 1
    if len(input_string) % 2 == 0:
        for i in range(mid, len(input_string)):
            r[ord(input_string[i]) - 97] += 1
    else:
        for i in range(mid + 1, len(input_string)):
            r[ord(input_string[i]) - 97] += 1
    flag = 1
    for i in range(0, 26):
        if l[i] != r[i]:
            print("NO")
            flag = 0
            break
    if flag:
        print("YES")
    t -= 1
