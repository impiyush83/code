"""
In how many steps can you get initial value to key by 2 operations:
1. appending 1 to the number
2. multiplying 2 to the number
"""


def find_transformation(init_val, number_to_find):
    """
    
    :param init_val: int
    :param number_to_find: int
    :return: 
    """
    if number_to_find == init_val:
        return 1
    if init_val > number_to_find:
        return 0
    ret_value1 = find_transformation(init_val * 10 + 1, number_to_find)
    ret_value2 = find_transformation(init_val * 2, number_to_find)
    return 1 if ret_value1 + ret_value2 == 1 else min(ret_value1,
                                                      ret_value2) + 1


if __name__ == "__main__":

    initial_value, key = list(map(int, input().split()))
    print(initial_value, key)

    if key == initial_value:
        print("Found")
        print("Steps: {steps}".format(steps=1))
    else:
        units_digit = key % 10
        if units_digit in [3, 5, 7, 9]:
            print("Units invalid stop")
            print('Not found')
        else:
            flag = find_transformation(initial_value, key)
            if flag:
                print('Found')
                print("Steps: {steps}".format(steps=flag))
            else:
                print('Not found')
