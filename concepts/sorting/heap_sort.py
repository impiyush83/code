def swift_up(S, i, operation):
    """
    Recursively does max_heapify
    :param S: list
    :param i: integer
    :param operation: string
    :return: max heap list
    """
    # dont recurse if index is 0
    if i < 1:
        return S

    # check parent is less than current
    if S[i // 2] < S[i] and operation == 'maxheap':
        # if yes swap
        S[i // 2], S[i] = S[i], S[i // 2]
        # apply swift up on parent
        return swift_up(S, i//2, operation)
    # for min heap
    if S[i // 2] > S[i] and operation == 'minheap':
        # if yes swap
        S[i // 2], S[i] = S[i], S[i // 2]
        # apply swift up on parent
        return swift_up(S, i // 2, operation)


def insertion(S, e, operation):
    """
    Inserts an element in the existing list and max_heapifies
    on S from index len(S) - 1
    :param S: list
    :param e: integer
    :param operation: string
    :return: None
    """
    S.append(e)
    i = len(S) - 1
    swift_up(S, i, operation)
    return S


if __name__ == '__main__':

    print("Max heap example: ")
    random_list = []
    random_list = insertion(random_list, 3, "maxheap")
    print(random_list)
    random_list = insertion(random_list, 8, "maxheap")
    print(random_list)
    random_list = insertion(random_list, 2, "maxheap")
    print(random_list)
    random_list = insertion(random_list, 1, "maxheap")
    print(random_list)
    random_list = insertion(random_list, 5, "maxheap")
    print(random_list)
    random_list = insertion(random_list, 10, "maxheap")
    print(random_list)

    print("Min heap example: ")
    random_list = []
    random_list = insertion(random_list, 3, "minheap")
    print(random_list)
    random_list = insertion(random_list, 8, "minheap")
    print(random_list)
    random_list = insertion(random_list, 2, "minheap")
    print(random_list)
    random_list = insertion(random_list, 1, "minheap")
    print(random_list)
    random_list = insertion(random_list, 5, "minheap")
    print(random_list)
    random_list = insertion(random_list, 10, "minheap")
    print(random_list)









