"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120 Output: 21 Note: Assume we are dealing with an environment which
could only store integers within the 32-bit signed integer range: [−231,
231 − 1]. For the purpose of this problem, assume that your function returns
0 when the reversed integer overflows. """


class Solution:
    def reverse(self, x: int) -> int:
        output_range = [-pow(2, 31), pow(2, 31) - 1]
        x = str(x)
        # string reverse
        x = x[::-1]
        if x[-1] == '-':
            # for negative numbers
            output = int("-" + x[0:-1])
        else:
            # for postive numbers
            output = int(x[:])
        if output < output_range[0] or output > output_range[-1]:
            return 0
        return output


if __name__ == "__main__":
    solution = Solution()
    input_num = int(input())
    print(solution.reverse(input_num))

#
# n = 4562
# rev = 0
#
# while n > 0:
#     a = n % 10
#     rev = rev * 10 + a
#     n = int(n / 10)
#
# print(rev)
