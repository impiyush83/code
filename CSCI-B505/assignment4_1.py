"""
Approach: 

1. Sort both lists in O(NlogN) by timsort

2. Iterate through  list1 and check if element doesnt exists in list2
by binary search in O(logN)

3. Iterate through  list2 and check if element doesnt exists in list1
by binary search in O(logN)

Time complexity - O(NlogN)

Eg: 

1.)

D1 = [10, 20, 30, 40, 40]

D2 = [10, 10, 20, 30, 40]

Output: Has same elements

2.)

D1 = [10, 50, 30, 40, 40]

D2 = [10, 10, 20, 30, 40]

Output: Does not have same set elements

"""

def binarysearch(list2: list, low: int, high: int, target: int):
    """
    Searches element by binary search
    :param list2: list
    :param low: integer
    :param high: integer
    :param target: integer
    :return: boolean
    """
    if low <= high:
        mid = (low + high) // 2
        if list2[mid] == target:
            return True
        elif list2[mid] < target:
            return binarysearch(list2, mid + 1, high, target)
        else:
            return binarysearch(list2, low, mid - 1, target)
    return False


def hasSameElements(list1: list, list2: list):
    """
    Checks whether 2 lists has same elements in O(N) time complexity
    :param list1: list
    :param list2: list
    :return: boolean
    """

    # takes O(NlogN)
    list1.sort()
    # takes O(NlogN)
    list2.sort()

    # takes O(N)
    for element in list1:
        # takes O(logN)
        if not binarysearch(list2, 0, len(list2) - 1, element):
            return False

    # takes O(N)
    for element in list2:
        # takes O(logN)
        if not binarysearch(list1, 0, len(list1) - 1, element):
            return False

    return True


if __name__ == '__main__':
    # print('Enter two lists:')
    # print("------------------")
    # print('sample input: ')
    # print('10 20 30 40 40')
    # print('20 30 40 50 60')
    # print("------------------")
    #D1, D2 = list(map(int, input().split())), list(map(int, input().split()))
    D1 = [1, 1, 2, 3]
    D2 = [2, 2, 1, 3]
    print(D1, D2)
    if hasSameElements(D1, D2):
        print("Has same set elements")
    else:
        print("Does not have same set elements")

    D1 = [1, 1, 2, 4]
    D2 = [2, 2, 1, 3]
    print(D1, D2)
    if hasSameElements(D1, D2):
        print("Has same set elements")
    else:
        print("Does not have same set elements")

