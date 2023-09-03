import util
import time
import PriorityQueue


def manhattenHeuristic(startState):
    return util.aStar(startState, manhattanDistance)


# Calculating Manhatten Distance for each node
def manhattanDistance(node):
    distance = 0
    for i in range(util.N):
        for j in range(util.N):
            if node.grid[i][j] != 0:  # Skip the empty space
                goal_i, goal_j = util.goalPositions[node.grid[i][j]]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance
