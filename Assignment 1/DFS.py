from collections import deque
import util
import time


def DFS(startState):
    startTimeBFS = time.time()
    allNodesVisited = []
    exploredDFS = {}
    noOfNodesChecked = 0
    frontier = deque()  # Maintaining Stack to Implement DFS
    frontier.append(startState)
    while frontier:
        noOfNodesChecked = noOfNodesChecked + 1  # Counting number of steps
        currentNode = frontier.pop()  # Use pop() for LIFO
        allNodesVisited.append(currentNode.grid)  # Adding all grid to print
        if util.isGoalState(currentNode.grid):  # checking if goal state reached
            totalTime = time.time() - startTimeBFS
            parentList = util.printParents(currentNode)  # Finding all parent Nodes
            parentList.reverse()
            return "YES", noOfNodesChecked, totalTime, parentList, allNodesVisited
        util.findSuccessor(frontier, currentNode, exploredDFS)
    totalTime = time.time() - startTimeBFS
    return "NO", noOfNodesChecked, totalTime, None, allNodesVisited
