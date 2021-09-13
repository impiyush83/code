import pdb

def search2D(grid, row, col, word):


    dir = [[-1, 0], [1, 0], [1, 1],
           [1, -1], [-1, -1], [-1, 1],
           [0, 1], [0, -1]]

    if grid[row][col] != word[0]:
        return False
    pdb.set_trace()

    for x, y in dir:
        pdb.set_trace()
        rd, cd = row + x, col + y
        flag = True

        for k in range(1, len(word)):

            if (0 <= rd <row and
                    0 <= cd < col and
                    word[k] == grid[rd][cd]):

                rd += x
                cd += y
            else:
                flag = False
                break
        if flag:
            return True
    return False


def patternSearch(row, col, grid, word):
    possible_points = []
    for r in range(row):
        for c in range(col):
            if search2D(grid, r, c, word):
                print(r, c)
                possible_points.append([r, c])
    return possible_points


t = int(input())
m, n = map(int, input().split())
matrix = []
for row in range(0, m):
    matrix.append(input().lower())

for i in matrix:
    print(i)
cases = int(input())
for case in range(cases):
    target_word = input().lower()
    possible_matches = patternSearch(m, n, matrix, target_word)
    print(possible_matches)
    # give leftmost
    # print
    pass



