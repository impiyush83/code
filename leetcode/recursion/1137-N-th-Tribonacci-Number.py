#recrursive
# def tribonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     data = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#     return data

# iterative
def tribonacci(n: int) -> int:
    tribonacci_list = [0, 1, 1]
    if n == 0 or n == 1 or n == 2:
        return tribonacci_list[n]

    dp_list_len = n + 1
    while len(tribonacci_list) != dp_list_len:
        tribonacci_list.append(tribonacci_list[-3] + tribonacci_list[-2] +
                               tribonacci_list[-1])
    print(tribonacci_list)
    return tribonacci_list[-1]


i = int(input())
print(tribonacci(i))
