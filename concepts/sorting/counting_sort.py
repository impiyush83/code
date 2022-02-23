def counting_sort(D, B, k):
    """
    This function implements counting sort algorithm
    :param D: unsorted sequence
    :param B: sorted sequence
    :param k: maximum element in D
    :return: sorted sequence B
    """
    C = []

    for i in range(0, k+1):
        C.append(0)

    input_length = len(D)

    print('C1 :', C)
    for j in range(0, input_length):
        C[D[j]] = C[D[j]] + 1

    print('C2 :', C)

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]

    print('C3 : ', C)

    print(C, D, B)

    for j in range(input_length-1, -1, -1):
        B[C[D[j]]] = D[j]
        C[D[j]] = C[D[j]] - 1
        print(B, D, C)

    print('B : ', B)

    return B[1:len(D)+1]


numbers = list(map(int, input().split()))
print("Input :", numbers)
sorted_numbers = counting_sort(numbers, [0] * (len(numbers)+1), max(numbers))
print("Output :", sorted_numbers)
