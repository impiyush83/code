from __future__ import print_function
import builtins


def print(number: int) -> None:
    """
    Hacks in-built print  function to print 114 if print(4)
    :param number: integer
    """
    if number == 4:
        builtins.print(112)
    else:
        builtins.print(0)


if __name__ == "__main__":
    print(4)
    # print(5)
