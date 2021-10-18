import math

"""

worst case time complexity - O(n^2)
worst case is when all elements are placed in a single bucket.

"""

def insertion_sort_subroutine(arr):
    """
    Sorts array by insertion sort
    :param arr:
    :return:
    """
    print("insertion sort", arr)
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    """
    Sorts array by buckets sort and buckets by insertion sort subroutine
    :param arr:
    :return:
    """
    bucket_size, buckets = len(arr), []
    for i in range(bucket_size):
        buckets.append([])

    for i in range(bucket_size):
        buckets[math.floor(bucket_size * arr[i])].append(arr[i])

    for i in range(bucket_size):
        buckets[i] = insertion_sort_subroutine(buckets[i])

    res = []
    for i in range(bucket_size):
        res += buckets[i]

    return res


if __name__ == '__main__':
    A = [0.9, 0.2, 0.1, 0.8, 0.15, 0.1]
    B = [0.1, 0.15, 0.5, 0.8, 0.9]
    print("For unordered sequence : ", A)
    print(bucket_sort(A))
    print("For ordered sequence : ", B)
    print(bucket_sort(B))