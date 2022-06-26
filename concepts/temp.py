



def ans():
    A = [1, 2, 2, 2, 4, 5, 6]
    B = [3, 5]

    def binarysearch(A, low, high, target):
        if low <= high:
            mid = (low + high) // 2

            if target == A[mid]:
                return mid
            elif target < A[mid]:
                return binarysearch(A, low, mid - 1, target)
            else:
                if target > A[mid - 1] and target < A[mid]:
                    return mid + 1
                elif target <= A[mid - 1]:
                    return binarysearch(A, low, mid - 1, target)
                else:
                    return binarysearch(A, mid + 1, high, target)
        return 0

    lenA = len(A)

    A = sorted(A)
    B = sorted(B)

    for item in B:
        if item >= A[-1]:
            yield lenA
        elif item < A[0]:
            yield 0
        elif item == A[0]:
            yield 1
        else:
            index = binarysearch(A, 0, len(A)-1, item)
            yield len(A) - index


for i in ans():
    print(i)