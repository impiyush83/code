MAX_DIGITS = 10


def check(freq, k):
    for i in range(0, MAX_DIGITS):
        if freq[i] and freq[i] != k:
            return False
    return True


def perfectSubstring(s, k):
    # Write your code here
    result = 0
    for i in range(0, len(s)):
        freq = [0] * MAX_DIGITS
        for j in range(i, len(s)):
            index = ord(s[j]) - ord('0')
            freq[index] += 1

            if freq[index] > k:
                break
            elif freq[index] == k and check(freq, k) == True:
                result += 1
    return result
