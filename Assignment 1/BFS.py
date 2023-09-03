from collections import deque
import util
import time


def BFS(startState):
    startTimeBFS = time.time()
    allNodesVisited = []
    exploredBFS = {}
    noOfNodesChecked = 0
    frontier = deque()  # Maintaining Queue to Implement BFS
    frontier.append(startState)
    while frontier:
        noOfNodesChecked = noOfNodesChecked + 1  # Counting number of steps
        currentNode = frontier.popleft()  # Use popleft() for FIFO
        allNodesVisited.append(currentNode.grid)  # Adding all grid to print
        if util.isGoalState(currentNode.grid):  # checking if goal state reached
            totalTime = time.time() - startTimeBFS
            parentList = util.printParents(currentNode)  # Finding all parent Nodes
            parentList.reverse()
            return "YES", noOfNodesChecked, totalTime, parentList, allNodesVisited
        util.findSuccessor(frontier, currentNode, exploredBFS)
    totalTime = time.time() - startTimeBFS
    return "NO", noOfNodesChecked, totalTime, None, None
