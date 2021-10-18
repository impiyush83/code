def merge_sort(arr):
    """
    Implements bottom up merge sort takes O(N^2 logN) here due to the extra
     while len(arr) != 1:  # O(N) iteration
    :param arr: list
    :return: list
    """
    size = 1
    while len(arr) != 1:  # O(N)
        D = []
        # size will always be of 2
        for i in range(0, len(arr), size*2):  # O(logN)
            # check if there is only one element left
            if len(arr)-1 != i:
                list1 = arr[i:i+size]
                list2 = arr[i+size:i+size*2]
                D = combine(list1, list2, D)  # O(N)
            else:
                S2 = []
                S1 = arr[i]
                # send default value -1
                S2.append(-1)
                D = combine(S1, S2, D)
        arr = D
    return arr

def combine(list1, list2, D):
    """
    Combines 2 queues by merging takes O(N) time due to merge function
    :param list1: list
    :param list2: list
    :param D: list
    :return: list
    """
    if list2[0] != -1:
        # sorting two queues by merging
        D.append(merge(list1, list2))
    else:
        # directly append if there is only one queue element
        # as it is already sorted
        D.append(list1)
    return D


def merge(list1, list2):
    """
    Merges list1 and list2 by queue based merging takes O(N) time
    :param list1: list
    :param list2: list
    :return: list
    """
    i, j, combined_list = 0, 0, []

    arr1 = [item for l1 in list1 for item in l1]
    arr2 = [item for l2 in list2 for item in l2]

    # queue is first in first out so 0th element
    # will be compared and every time and pop
    # will always happen at 0th index
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            combined_list.append(arr1.pop(0))
            i += 1
        else:
            combined_list.append(arr2.pop(0))
            j += 1
    # check if S1 queue has any elements left
    while arr1:
        combined_list.append(arr1.pop(0))
    # check if S2 queue has any elements left
    while arr2:
        combined_list.append(arr2.pop(0))
    return combined_list


if __name__ == '__main__':
    S1 = [[1], [5], [4], [2], [3]]
    S2 = [[1], [1], [2], [2], [3]]
    print("For ordered sequence : ", S2)
    S2 = merge_sort(S2)
    print(S2)
    print("For unordered sequence : ", S1)
    S1 = merge_sort(S1)
    print(S1)
