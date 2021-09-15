#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    z = [add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0, len(house_map[0])) if house_map[r][c] == '.']
    print(len(z))
    return z


def findAllPichus(house_map):
    return [[row_i, col_i] for col_i in range(len(house_map[0])) for row_i in
     range(len(house_map)) if house_map[row_i][col_i] == "p"]


def isPichusPlacementValid(house_map):
    print(house_map)
    pichus = findAllPichus(house_map)
    for pichu in pichus:
        # right
        row = pichu[0]
        col = pichu[1]
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
    return True

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k and isPichusPlacementValid(house_map)

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors(fringe.pop()):
            print(fringe)
            if is_goal(new_house_map, k):
                return(new_house_map,True)
            fringe.append(new_house_map)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map, k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")

