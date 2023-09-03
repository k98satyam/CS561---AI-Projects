import MisplacedTile
import NodeStructure
import util
import ManhattanDistance

i = 1
if __name__ == '__main__':
    while i != 0:
        i -= 1
        grid, randomRow, randomCol = util.generateRandomGrid()
        start = NodeStructure.Node(None, grid, [randomRow, randomCol], 1, 0)
        # manhatten dis sol
        # start = NodeStructure.Node(None, [[7, 4, 3],[8, 1, 5],[0, 2, 6]], [2, 0], 1, 0)
        # start = NodeStructure.Node(None, [[1, 5, 2],[4, 0, 3],[7, 8, 6]], [1, 1], 1, 0)  -- both true
        # misplaced sol
        # start = NodeStructure.Node(None, [[3, 6, 8],[2, 0, 5],[1, 4, 7]], [1, 1], 1, 0)
        # start = NodeStructure.Node(None, [[6, 8, 7],[3, 1, 5],[2, 4, 0]], [2, 2], 1, 0)
        # start = NodeStructure.Node(None, [[3, 6, 8], [5, 7, 0], [2, 1, 4]], [1, 2], 1, 0)

        print("Initial Grid Configuration-")
        for configGrid in grid:
            print(configGrid)
        print("Goal Grid Configuration-")
        for goalRow in util.goal:
            print(goalRow)
        start.costTillNow = ManhattanDistance.manhattanDistance(start)
        MDNode, MDStep = ManhattanDistance.HillClimbing(start)

        start.costTillNow = MisplacedTile.calculateCosts(start)
        MTNode, MTStep = MisplacedTile.HillClimbing(start)

        print("Solution Found using Manhatten Distance - ", util.isGoalState(MDNode.grid))
        print("Number of steps taken - ", MDStep)
        MD = input("Do you want to see parent list(y/n) - ")
        if MD == "y":
            parent = util.printParents(MDNode)
            parent.reverse()
            print(parent)
        print("---------------------------------------------------------------------------------------")

        print("Solution Found using Misplaced Tile - ", util.isGoalState(MTNode.grid))
        print("Number of steps taken - ", MTStep)
        MT = input("Do you want to see parent list(y/n) - ")
        if MT == "y":
            parent = util.printParents(MTNode)
            parent.reverse()
            print(parent)
        print("---------------------------------------------------------------------------------------")

        # if MTNode.grid == util.goal:
        #     i = 0
