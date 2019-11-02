for i in range(int(input())):
    n = int(input())
    string1 = str(input())
    if n == 1:
        print(string1.count('1'))
    else:
        temp = string1
        for j in range(n-1):
            string2 = str(input())
            y = int(temp, 2) ^ int(string2, 2)
            temp = str(bin(y)[2:].zfill(len(temp)))
        print(temp.count('1'))
