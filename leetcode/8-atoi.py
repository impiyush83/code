class Solution:
    def my_Atoi(self, string: str) -> int:
        s = ""
        string = string.strip()
        for i, x in enumerate(string):
            # check for the + and - sign else append if isdigit else break
            if x in ["-", "+"] and s == "" and len(string[i:]) > 1 and string[i + 1].isdigit():
                s += x
            elif x.isdigit():
                s += x
            else:
                break
        # if empty return 0
        if s == "":
            return 0
        try:
            s = int(s)
        except:
            return 0
        # for 32 bit number limit
        INT_MIN = (2 ** 31) * -1
        INT_MAX = (2 ** 31) - 1
        if s < INT_MIN:
            return INT_MIN
        elif s > INT_MAX:
            return INT_MAX
        else:
            return s
