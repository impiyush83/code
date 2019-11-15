from typing import List


class Solution:
    def toInt(self, num_list):
        string = ""
        for i in num_list:
            string += str(i)
        return int(string)

    def incr(self, num):
        return num + 1

    def toList(self, num):
        temp = []
        for i in str(num):
            temp.append(int(i))
        return temp

    def plusOne(self, digits: List[int]) -> List[int]:
        num = self.toInt(digits)
        print(num)
        num = self.incr(num)
        return self.toList(num)
