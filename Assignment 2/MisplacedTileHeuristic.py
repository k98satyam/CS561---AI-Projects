import util
import time
import PriorityQueue


def misplacedHeuristic(startState):
    return util.aStar(startState, calculateCosts)


# To calculate cost, ie number of misplaced tile
# here h(n) = number of misplaces tile
def calculateCosts(node):
    count = 0
    for i in range(util.N):
        for j in range(util.N):
            if node.grid[i][j] and node.grid[i][j] != util.goal[i][j]:
                count += 1
    return count
