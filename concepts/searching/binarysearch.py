def binarysearch_recursive(array, lower, upper, key):
    if upper >= lower:
        mid = int(lower + (upper - lower) / 2)
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            return binarysearch_recursive(array, mid + 1, upper, key)
        else:
            return binarysearch_recursive(array, lower, mid - 1, key)
    else:
        return -1


def binarysearch_iterative(array, lower, upper, key):
    while (upper >= lower):
        mid = int(lower + (upper - lower) / 2)
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            lower = mid + 1
        else:
            upper = mid - 1
    else:
        return -1


# Binary Search recursive - O(logn)
# Binary Search iterative - O(n/2) -> O(n)

if __name__ == "__main__":
    # array as integers
    arr = list(map(int, input().split()))
    # target value to find
    target = int(input())
    lower = 0
    upper = len(arr) - 1
    print(binarysearch_recursive(arr, lower, upper, target))
