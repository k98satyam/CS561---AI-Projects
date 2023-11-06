import time

import NodeStructure
import simulatedAnnealing
import util

if __name__ == '__main__':
    while True:
        randonGrid, randomRow, randomCol = util.generateRandomGrid()
        # start = NodeStructure.Node(None, [[2, 5, 3], [4, 8, 1], [7, 0, 6]], [2, 1], 0)
        start = NodeStructure.Node(None, randonGrid, [randomRow, randomCol], 0)
        start.costTillNow = util.manhattanDistance(start)
        print("Initial Grid Configuration-")
        for configGrid in start.grid:
            print(configGrid)
        print("Goal Grid Configuration-")
        for goalRow in [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print(goalRow)

        start.costTillNow = util.misplacedTile(start)
        startTime = time.time()
        lastState, goalFound, steps = simulatedAnnealing.simulatedAnnealing(start, util.misplacedTile)
        print("Misplaced Tile")
        print(lastState.grid, goalFound, steps, time.time() - startTime)
        print("----------------------------------------------------------------------------------------")
        print("Manhattan Distance")
        start.costTillNow = util.manhattanDistance(start)
        startTime = time.time()
        lastState, goalFound, steps = simulatedAnnealing.simulatedAnnealing(start, util.manhattanDistance)
        print(lastState.grid, goalFound, steps, time.time() - startTime)
        # if goalFound != "NO":
        #     break
        break
