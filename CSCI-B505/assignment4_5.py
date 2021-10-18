"""

Time complexity - (NlogN)
N = number of elements

"""


def max_heapify(H: list, i: int):
    """
    Heapify operation
    :param H: list
    :param i: int
    :return: None
    """
    # take left and right elements
    left = 2 * i + 1
    right = 2 * i + 2
    # assign index i to largest by default
    largest = i

    if left < heap_size and H[left] > H[i]:
        largest = left

    if right < heap_size and H[right] > H[largest]:
        largest = right

    if largest != i:
        # if largest is changed swap largest and ith element
        H[i], H[largest] = H[largest], H[i]
        # apply max heap on largest index
        max_heapify(H, largest)

def build_max_heap(H):
    """
    Builds max heap
    :param H: list
    :return: None
    """
    # start from mid element and apply heapify here which is max_heap
    for i in range(heap_size // 2, -1, -1):
        # apply max heap on ith index
        max_heapify(H, i)


def heap_sort(H):
    """
    Sorts the H via heap sort
    :param H: list
    :return: None
    """
    global heap_size
    heap_size = len(H)
    build_max_heap(H)
    for i in range(heap_size - 1, 0, -1):
        # swap first and last element
        H[0], H[i] = H[i], H[0]
        # dont consider last element
        heap_size -= 1
        # apply heap on first index of H
        max_heapify(H, 0)


if __name__ == '__main__':
    D1 = [1, 1, 2, 3, 4]  # ordered sequence
    D2 = [1, 3, 2, 3]  # unordered sequence
    print("For ordered sequence : ", D1)
    heap_sort(D1)
    print(D1)
    print("For unordered sequence : ", D2)
    heap_sort(D2)
    print(D2)