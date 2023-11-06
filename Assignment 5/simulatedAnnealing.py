import random
import math

import util


def exponential_decay(T):
    return 0.01 * T


def acceptanceProb(temp, deltaEng):
    alpha = 0.25
    return math.exp((-alpha * deltaEng) / temp)


def simulatedAnnealing(start, costFunction):
    explored = {tuple(tuple(row) for row in start.grid): 1}
    steps = 0
    itr = 1000
    temperature = itr
    currentNode = start
    while temperature >= 0:
        neighbours = util.findSuccessor(currentNode, costFunction, explored)
        itr -= 1
        temperature = exponential_decay(itr)
        # print(temperature)
        nextNodeAccepted = False
        bestNodeHere = start
        steps += 1
        for i in neighbours:
            # print(i.grid)
            if util.isGoalState(i.grid):
                return i, "GOAL FOUND", steps
            deltaEnergy = currentNode.costTillNow - i.costTillNow
            # print("deltaEnergy", deltaEnergy, "currentNode.costTillNow", currentNode.costTillNow, "i.costTillNow", i.costTillNow)
            if deltaEnergy > 0:
                bestNodeHere = i
                break
            else:
                prob = acceptanceProb(temperature, deltaEnergy)
                if random.uniform(0.0, 1.0) < prob:
                    bestNodeHere = i
                    break
            if not nextNodeAccepted:
                bestNodeHere = start
        currentNode = bestNodeHere
    return currentNode, "NO", steps
