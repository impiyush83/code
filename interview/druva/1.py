input1 = int(input())
input3 = list(map(int, input().split()))
l = []
maxi = input1
for i in range(0, input1 + 1):
    if i not in input3:
        l.append(i)
l.sort()
sum = 0
cnt = 0
for i in l:
    if sum < maxi:
        sum += i
        cnt += 1
    else:
        break
