"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            cur = 1
            len_x = len(str(x)) - 1
            old_x = x
            new_num = 0
            while x != 0:
                new_num += pow(10, len_x) * (x % 10)
                # print(new_num)
                len_x -= 1
                x = int(x / 10)
            # print(old_x, new_num)
            if new_num == old_x:
                return True
            else:
                return False


if __name__ == "__main__":
    solution = Solution()
    input_num = int(input())
    print(solution.isPalindrome(input_num))
