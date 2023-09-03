import util
import time
import PriorityQueue


def zeroHeuristic(startState):
    return util.aStar(startState, zeroHeuristicCostFunction)


def zeroHeuristicCostFunction(node):
    return 0
