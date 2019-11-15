def fun(n, noOpeningB, noClosingB, stringFormed):
    if noOpeningB == n and noClosingB == n:
        print(stringFormed)
        return

    if stringFormed:
        if stringFormed[0] == '}':
            return

    if noOpeningB < noClosingB:
        return

    if noOpeningB != n:
        fun(n, noOpeningB + 1, noClosingB, stringFormed + '{')

    if noClosingB != n:
        fun(n, noOpeningB, noClosingB + 1, stringFormed + '}')


n = int(input())
fun(n, 0, 0, '')
