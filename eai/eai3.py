#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [Nikhil Kamble - nkamble]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

global N
N = 4


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in
                f.read().rstrip("\n").split("\n")][3:]


# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([row.count('p') for row in house_map])


# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])


# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [
        house_map[row][0:col] + ['p', ] + house_map[row][col + 1:]] + house_map[
                                                                      row + 1:]


# To check whether two agents(aka pichu) can see each other in a row/column/diagonal
def check_pichu_position(house_map, row, col):
    # checking pichu in same row/column/diagonal

    # ======================================================================
    # for i,j in zip(range(col-1,-1,-1), range(col+1,len(house_map[0]))):
    #     if(house_map[row][i] == 'p' or house_map[row][j] == 'p'):
    #         return False

    # for i,j in zip(range(row-1,-1,-1), range(row+1,len(house_map))):
    #     if(house_map[i][col] == 'p' or house_map[j][col] == 'p'):
    #         return False
    # =======================================================================

    # for i in range(col):
    # print('for madhe',row, col)
    # if(row<len(house_map) and col<len(house_map[0])):
    #     if(house_map[row][col] == 'p' or house_map[row][col+1] == 'p' or house_map[row][col-1] == 'p' or house_map[row+1][col] == 'p' or house_map[row-1][col] == 'p'):
    #         return False

    # for i in range(row):
    #     if(house_map[i][col] == 'p' or house_map[i+1][col] == 'p' or house_map[i-1][col] == 'p'):
    #         return False

    # for i in range(len(house_map)):
    #     if(house_map[i][col] == 'p' and house_map[i-1][col] == 'p'):
    #         print('checking - left')
    #         return False

    # for i in range(len(house_map)):
    #     if(house_map[i][col] == 'p' and house_map[i+1][col] == 'p'):
    #         print('checking - right')
    #         return False

    #     if( (house_map[i][j] == 'p' and house_map[i-1][j] == 'p') or (house_map[i][j] == 'p' and house_map[i+1][j] == 'p')):
    #             print('checking - left and right')
    #             return False
    #     if( (house_map[i][j] == 'p' and house_map[i-1][j-1] == 'p') or (house_map[i][j] == 'p' and house_map[i+1][j+1] == 'p')):
    #             print('checking - upper left and bottom right')
    #             return False
    #     if( (house_map[i][j] == 'p' and house_map[i-1][j+1] == 'p') or (house_map[i][j] == 'p' and house_map[i+1][j-1] == 'p')):
    #             print('checking - bottom left and upper right')
    #             return False
    # return True
    pass


def isPichusPlacementValid(house_map, row, col):
    for i in range(col + 1, len(house_map[0])):
        if house_map[row][i] == 'p':
            return False
        if house_map[row][i] == 'X' or house_map[row][i] == '@':
            break
    # left
    for i in range(col - 1, -1, -1):
        if house_map[row][i] == 'p':
            return False
        if house_map[row][i] == 'X' or house_map[row][i] == '@':
            break
    # top
    for i in range(row - 1, -1, -1):
        if house_map[i][col] == 'p':
            return False
        if house_map[i][col] == 'X' or house_map[row][i] == '@':
            break
    # bot
    for i in range(row + 1, len(house_map)):
        if house_map[i][col] == 'p':
            return False
        if house_map[i][col] == 'X' or house_map[row][i] == '@':
            break
    # diagonal topright
    temprow = row
    tempcol = col
    temprow -= 1
    tempcol += 1
    while temprow <= 0 and tempcol < len(house_map[0]):
        if house_map[temprow][tempcol] == 'p':
            return False
        if house_map[temprow][tempcol] == 'X' or house_map[temprow][
            tempcol] == '@':
            break
        temprow -= 1
        tempcol += 1
    # diagonal topleft
    temprow = row
    tempcol = col
    temprow -= 1
    tempcol -= 1
    while temprow >= 0 and tempcol >= 0:
        if house_map[temprow][tempcol] == 'p':
            return False
        if house_map[temprow][tempcol] == 'X' or house_map[temprow][
            tempcol] == '@':
            break
        temprow -= 1
        tempcol -= 1
    # diagonal bottom left
    temprow = row
    tempcol = col
    temprow += 1
    tempcol -= 1
    while temprow < len(house_map) and tempcol >= 0:
        if house_map[temprow][tempcol] == 'p':
            return False
        if house_map[temprow][tempcol] == 'X' or house_map[temprow][
            tempcol] == '@':
            break
        temprow += 1
        tempcol -= 1

    # diagonal bottom right
    temprow = row
    tempcol = col
    temprow += 1
    tempcol += 1
    while temprow < len(house_map) and tempcol < len(house_map[0]):
        if house_map[temprow][tempcol] == 'p':
            return False
        if house_map[temprow][tempcol] == 'X' or house_map[temprow][
            tempcol] == '@':
            break
        temprow += 1
        tempcol += 1
    return True


# Get list of successors of given house_map state
def successors(house_map):
    return [add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c
            in range(0, len(house_map[0])) if
            house_map[r][c] == '.' and isPichusPlacementValid(house_map, r, c)]
    # and check_pichu_position_col(house_map, r, c)


# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map, k):
    fringe = [initial_house_map]
    # visited_node = []
    while len(fringe) > 0:
        for new_house_map in successors(fringe.pop()):
            if is_goal(new_house_map, k):
                print('Found !!!!!')
                return (new_house_map, True)
            # if new_house_map not in visited_node:
            #     visited_node.append(new_house_map)
            fringe.append(new_house_map)
    # return False
    return False, ''


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print("Starting from initial house map:\n" + printable_house_map(
        house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map, k)
    print("Here's what we found:")
    print(printable_house_map(solution[0]) if solution[1] else "False")
