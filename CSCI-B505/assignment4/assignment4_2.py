"""

Approach:

As there exists n^2 max number in list of elements, if we do just counting sort
then the time complexity of counting sort will be O(n^2) as time complexity of
counting sort is O(N) generally.

We use radix sort to solve this problem this reduces the time complexity
drastically.

Time complexity: O(D * (N + k))
D = number of digits of max element of array
N = Number of elements

the D is almost a constant due to N^2 - 1 condition, hence it can be neglected

Time complexity is near to O(N).

"""
def counting_sort_subroutine(arr: list, k: int):
    """
    The returns sorted list based on k index
    :param arr: list
    :param k: integer
    :return: list
    """
    DIGITS = 10
    n = len(arr)
    # initialize
    output, digit_occurence_counter = [0] * n, [0] * DIGITS
    print("k", k)
    # counter from 0 to 9 indexes increments by 1
    for j in range(0, n):
        # find the digit of unit, tens , hundreds based on k
        index = arr[j] // k
        # increment the occurence of that digit
        digit_occurence_counter[index % DIGITS] += 1

    # gets cumulative sum
    for j in range(1, 10):
        digit_occurence_counter[j] += digit_occurence_counter[j - 1]

    # sorts and puts into output
    for j in range(n - 1, -1, -1):
        index = arr[j] // k
        output[digit_occurence_counter[index % DIGITS] - 1] = arr[j]
        digit_occurence_counter[index % DIGITS] -= 1

    return output


def radix_sort(arr: list, maxi: int):
    """
    Implementation of radix sort
    :param arr: list
    :param maxi: integer
    :return: list
    """
    D2 = arr
    # iterate through the 0 to length of max number in arr
    for i in range(0, maxi):
        print("pass ", i + 1)
        # apply counting sort on D2 wrt the radix pow(10 ,i) th digit
        D2 = counting_sort_subroutine(D2, pow(10, i))
        print(D2)
    return D2


if __name__ == '__main__':
    # print('Enter list:')
    # print("------------------")
    # print('sample input: ')
    # print('70 30 40 50 60')
    # print("------------------")
    #
    # D1 = list(map(int, input().split()))
    D1 = [0, 1, 11, 101, 100, 500, 503]
    print(D1)
    # send input array and length of max element in the array
    radix_sort(D1,  len(str(max(D1))))
    D2 = [0, 10, 3, 51, 23, 22]
    print(D2)
    radix_sort(D1, len(str(max(D2))))