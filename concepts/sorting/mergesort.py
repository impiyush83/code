def mergesort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i = 0
    j = 0
    k = l  # index of last merged array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


a = [1, 10, 7, 4, 3, 2]
mergesort(a, 0, 5)
print(a)
