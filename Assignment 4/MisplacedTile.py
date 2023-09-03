import util
import random


def HillClimbing(node):
    curr = node
    step = 0
    bestNeighbour = random.choice(util.findSuccessor(curr, calculateCosts))  # Initialize bestNeighbour with a valid neighbor
    visited = [tuple(tuple(row) for row in curr.grid)]
    while True:
        step += 1
        neighbours = util.findSuccessor(curr, calculateCosts)
        sameCostNeighbour = []
        for neighbour in neighbours:
            testNode = tuple(tuple(row) for row in neighbour.grid)
            if testNode not in visited:
                if neighbour.costTillNow < bestNeighbour.costTillNow:
                    bestNeighbour = neighbour
                    sameCostNeighbour = []  # emptying since found better sol
                elif neighbour.costTillNow == curr.costTillNow:
                    sameCostNeighbour.append(neighbour)
        if bestNeighbour.costTillNow >= curr.costTillNow:
            if sameCostNeighbour:
                # Allow a sideways move to a neighbor with the same cost
                curr = random.choice(sameCostNeighbour)
                visited.append(tuple(tuple(row) for row in curr.grid))
                continue
            else:
                # Stuck in a local optimum, break out of the loop
                break
        else:
            curr = bestNeighbour
            visited.append(tuple(tuple(row) for row in curr.grid))
    return curr, step


def calculateCosts(node):
    count = 0
    for i in range(util.N):
        for j in range(util.N):
            if node.grid[i][j] and node.grid[i][j] != util.goal[i][j]:
                count += 1
    return count
