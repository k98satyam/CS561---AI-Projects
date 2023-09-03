import ManhattanDistanceHeuristic
import util
import random


def incorrectHeuristic(startState):
    return util.aStar(startState, calculateIncorrectCosts)


# to calculate incorrect heuristic
def calculateIncorrectCosts(node):
    cost = node.costTillNow + ManhattanDistanceHeuristic.manhattanDistance(node) + random.randint(10, 100)
    return cost
