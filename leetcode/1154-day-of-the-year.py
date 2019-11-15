class Solution:
    def dayOfYear(self, date: str) -> int:
        leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = list(map(int, date.split('-')))
        is_leap = False

        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            is_leap = True

        if year % 4 == 0 and year % 100 != 0:
            is_leap = True

        if is_leap:
            ans = sum(leap[0:month - 1])
        else:
            ans = sum(non_leap[0:month - 1])
        ans += day
        return ans