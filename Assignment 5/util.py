import NodeStructure
import copy
import random
import time

N = 3
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goalPositions = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1],
                 0: [2, 2]}  # Dictionary to store goal positions of each number


# Checking if given row, col value is valid values
def isValid(row, col):
    return 0 <= row < N and 0 <= col < N


# Checking if goal state or not
def isGoalState(currentGrid):
    return currentGrid == goal


# Generate Randon Grid
def generateRandomGrid():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    grid = [numbers[i:i + 3] for i in range(0, 9, 3)]
    randomRow = -1
    randomCol = -1
    for rowItr, row in enumerate(grid):
        for colItr, col_value in enumerate(row):
            if col_value == 9:
                randomRow = rowItr
                randomCol = colItr
                grid[randomRow][randomCol] = 0
    return grid, randomRow, randomCol


# Generating all valid successor a particular node
# and adding it to frontier if that node has not been visited
def findSuccessor(node, costFunction, explored):
    frontier = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        newRow = node.emptyTile[0] + dr[i]
        newCol = node.emptyTile[1] + dc[i]
        if isValid(newRow, newCol):
            newNode = NodeStructure.Node(node, copy.deepcopy(node.grid), [], 0)
            newNode.grid[node.emptyTile[0]][node.emptyTile[1]], newNode.grid[newRow][newCol] = newNode.grid[newRow][
                newCol], newNode.grid[node.emptyTile[0]][node.emptyTile[1]]
            newNode.emptyTile = [newRow, newCol]
            newNode.costTillNow = costFunction(newNode)
            searchState = tuple(tuple(row) for row in newNode.grid)
            if searchState not in explored:
                frontier.append(newNode)
                explored[searchState] = 1
    return frontier


# return all parent nodes of a particular node
def printParents(node):
    parentList = []
    current = node
    while current is not None:
        parentList.append(current.grid)
        current = current.parent
    return parentList


def misplacedTile(node):
    count = 0
    for i in range(N):
        for j in range(N):
            if node.grid[i][j] and node.grid[i][j] != goal[i][j]:
                count += 1
    return count


# Calculating Manhatten Distance for each node
def manhattanDistance(node):
    distance = 0
    for i in range(N):
        for j in range(N):
            if node.grid[i][j] != 0:  # Skip the empty space
                goal_i, goal_j = goalPositions[node.grid[i][j]]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance


