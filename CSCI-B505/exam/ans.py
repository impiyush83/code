def calc(n):
    k=0  # 1 times
    i = n/2 # 1 times
    while(i<=n):  # this will run N / 2 times
        i= i + 1 # N / 2 times
        j=2  # N / 2 times
        while(j<=n): # this will run ((N / 2) * log N) times
            j=j*2  # this will run ((N / 2) * log N) times
            k = k + n/2 # this will run ((N / 2) * log N) times
    return k # 1 times

print(calc(int(input())))

# # total time complexity is (N * log N)