from collections import Counter

def getSubstrings(s):
    all_substrings = []
    for i in range(0, len(s)):
        for j in range(0, len(s) - i):
            sub_string = s[j:j + i + 1]
            if sub_string not in all_substrings:
                yield sub_string


def perfectSubstring(s, k):
    result = 0
    for substring in getSubstrings(s):
        freq_count = Counter(substring)
        flag = 1
        for element in freq_count:
            if freq_count[element] != k:
                flag = 0
                break
        if flag:
            result += 1
    return result


s = input()
k = int(input())
print(perfectSubstring(s, k))
