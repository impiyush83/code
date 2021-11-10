import random
import string
import time

"""
## Have fun with the three algorithms
### Understand each algorithm
- read algorithm implementations

### Thins you can change
- Letter set: small set (eg "ATGC") vs large set (eg. all letters string.letters)
- Pattern: random string vs string with certain pattern
    - pattern size
    - kmp failure function
    
### Explore
- When Boyer-Moore is fastest
- When Boyer-Moore is slowest
- When KMP is fastest
"""

def generate_random_strings(letters, size):
    return ''.join(random.choice(letters) for i in range(size))


# Brute force
def find_brute(T, P):
    n, m = len(T), len(P)
    # every starting position
    for i in range(n-m+1):
        k = 0
        # conduct O(k) comparisons
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1

# Boyer-Moore
def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i < n:
        # If match, decrease i,k
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        # Not match, reset the positions
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1
    return -1


# KMP failure function
def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def find_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    # print(fail)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j-m+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1

def compare(T, P):

    startTime = time.time()
    index = find_brute(T, P)
    endTime = time.time()
    print("Brute force takes {:f}s to run and returns {:d}".format(endTime-startTime, index))

    startTime = time.time()
    index = find_boyer_moore(T, P)
    endTime = time.time()
    print("Boyer More takes {:f}s to run and returns {:d}".format(endTime-startTime, index))

    startTime = time.time()
    index = find_kmp(T, P)
    endTime = time.time()
    print("KMP takes {:f}s to run and returns {:d}".format(endTime-startTime, index))


random.seed(100)

# Play with letter_set
letter_set = string.ascii_letters

random_string = generate_random_strings(letter_set, 10**7)
pattern = generate_random_strings("ATGC", 100)

# test string 1 when pattern is at the last
test_string1 = random_string + pattern

test_string2 = pattern + random_string

test_string3 = random_string + pattern + random_string

compare(test_string1, pattern)
compare(test_string2, pattern)
compare(test_string3, pattern)


pattern = generate_random_strings(letter_set, 100)

test_string1 = random_string + pattern

test_string2 = pattern + random_string

test_string3 = random_string + pattern + random_string

compare(test_string1, pattern)
compare(test_string2, pattern)
compare(test_string3, pattern)