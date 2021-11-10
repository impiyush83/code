"""

Approach:

We store all the items in dictionary and increment the default value 0 initally
by 1

Space Complexity is O(N)
Time complexity is O(N).

"""

from collections import defaultdict

def hasTwoEqualElements(list1):
    """
    Checks whether a list has two equal elements in O(N) time complexity
    :param list1: list
    :return: boolean
    """
    dicto1= defaultdict(lambda: 0)
    for i in list1: dicto1[i] += 1
    for key in dicto1.keys():
            if dicto1[key] > 1:
                return True
    return False


if __name__ == '__main__':
    # D1 = list(map(int, input().split()))
    D1 = [1, 2, 3, 4]
    print(D1)
    if hasTwoEqualElements(D1):
        print("Has two equal elements")
    else:
        print("Does not have two equal elements")
    D2 = [2, 2, 3, 3]
    print(D2)
    if hasTwoEqualElements(D2):
        print("Has two equal elements")
    else:
        print("Does not have two equal elements")