import numpy as np


def knapsack_dynamic(items, weight, number_items, curr_item):
    """
    Builds a DP table by top down approach
    :param items: list
    :param weight: int
    :param number_items: int
    :param curr_item: int
    :return: list
    """
    x = number_items - curr_item - 1
    y = weight

    if curr_item >= number_items or weight <= 0:
        return 0

    if dp[x][y] != 0:
        return dp[x][y]

    if weight < items[curr_item]:
        dp[x][y] = knapsack_dynamic(
            items,
            weight,
            number_items,
            curr_item + 1
        )
    else:
        dp[x][y] = max(
            items[curr_item] +
            knapsack_dynamic(
                items,
                weight - items[curr_item],
                number_items,
                curr_item + 1
            ),
            knapsack_dynamic(
                items,
                weight,
                number_items,
                curr_item + 1
            )
        )
    return dp[x][y]


def backtrack(max_value_obtained, knapsack_size, items, number_items):
    """
    Backtracks through DP table to find the items of the subset that sums
    closest to knapsack_size
    :param max_value_obtained: int
    :param knapsack_size: int
    :param items: list
    :param number_items: int
    :return: None
    """
    print("Subset of weights which sum up to {} are:".format(knapsack_size))
    ans = []
    for i in range(number_items - 1, 0, -1):
        if max_value_obtained <= 0:
            break

        if max_value_obtained - items[number_items - i - 1] \
                == dp[i - 1][knapsack_size - items[number_items - i - 1]]:
            ans.append(items[number_items - i - 1])
            index = number_items - i
            max_value_obtained -= items[number_items - i - 1]
            knapsack_size -= items[number_items - i - 1]

    if knapsack_size > 0:
        temp = items[index:]
        if knapsack_size > min(temp):
            temp2 = np.array([knapsack_size] * len(temp)) - np.array(temp)
            for i in range(len(temp2)):
                if temp2[i] < 0:
                    temp2[i] = 10000
            ans.append(items[list(temp2).index(min(temp2)) + index])
    print(ans)


if __name__ == "__main__":
    items = [5, 23, 27, 37, 48, 51, 63, 67, 71, 75, 70, 83, 889, 91, 101, 112,
             121, 132, 137, 141, 143, 147, 153, 159, 171, 181, 190, 191]
    print("Bag of items :", sorted(items))
    print("Total Item sum is : ", sum(items))
    knapsack_size = 762
    print("Enter knapsack size: ")
    if knapsack_size > sum(items):
        print("Items picked are :", items)
    else:
        number_items = len(items)
        dp = [[0 for _ in range(knapsack_size + 1)] for __ in range(number_items + 1)]
        max_value_obtained = knapsack_dynamic(items, knapsack_size, number_items, 0)
        print("Knapsack size", knapsack_size)
        print("Max value obtained", max_value_obtained)
        backtrack(max_value_obtained, knapsack_size, items, number_items)

