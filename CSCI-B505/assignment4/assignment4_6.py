"""

Time complexity - 0(N)
N = max number of the input list

"""

def counting_sort(D, B, k):
    """
    This function implements counting sort algorithm
    :param D: unsorted sequence
    :param B: sorted sequence
    :param k: maximum element in D
    :return: sorted sequence B
    """
    C = []
    # first append C all with 0 times max number in unsorted sequence
    for i in range(0, k + 1):
        C.append(0)

    input_length = len(D)

    print('C1 :', C)

    # increment the occurence index in C by 1
    for j in range(0, input_length):
        C[D[j]] = C[D[j]] + 1

    print('C2 :', C)

    # take cumulative sum of C
    for i in range(1, k + 1):
        C[i] = C[i] + C[i-1]

    print('C3 : ', C)
    # put into B the output array
    for j in range(input_length-1, -1, -1):
        B[C[D[j]] - 1] = D[j]
        C[D[j]] = C[D[j]] - 1

    print('B : ', B)
    return B


if __name__ == '__main__':
    D1 = [1, 1, 2, 3, 4]  # ordered sequence
    D2 = [1, 3, 2, 3]  # unordered sequence
    print("For ordered sequence : ", D1)
    D1 = counting_sort(D1, [0] * len(D1), max(D1))
    print(D1)
    print("For unordered sequence : ", D2)
    D2 = counting_sort(D2, [0] * len(D2), max(D2))
    print(D2)