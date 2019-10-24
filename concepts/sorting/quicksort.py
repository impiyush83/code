def partition(arr, lower, upper):
    pivot = arr[upper]
    i = lower - 1
    for j in range(lower, upper):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[upper] = arr[upper], arr[i+1]
    return i+1


def quicksort(arr, lower, upper):
    if upper > lower:
        pi = partition(arr, lower, upper)
        quicksort(arr, lower, pi - 1)
        quicksort(arr, pi + 1, upper)

# inplace algorithm
# Best O(nlogn)


if __name__ == "__main__":
    # array as integers
    arr = list(map(int, input().split()))
    quicksort(arr, 0, len(arr)-1)
    print(arr)
