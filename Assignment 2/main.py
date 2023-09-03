import NodeStructure
import ZeroHeuristic
import MisplacedTileHeuristic
import ManhattanDistanceHeuristic
import IncorrectHeuristic
import util

if __name__ == '__main__':
    # grid, randomRow, randomCol = util.generateRandomGrid()
    start = NodeStructure.Node(None, [[2, 5, 7], [4, 8, 1], [8, 6, 1]], [1, 1],1, 1)
    # start = NodeStructure.Node(None, [[5, 2, 6],[0, 7, 8],[4, 1, 3]], [1, 0],1, 1)
    # start = NodeStructure.Node(None, grid, [randomRow, randomCol], 1, 1)
    # print("Initial Grid Configuration-")
    # for configGrid in grid:
    #     print(configGrid)
    print("Goal Grid Configuration-")
    for goalRow in util.goal:
        print(goalRow)

    # calculating manhattan first, because if this fails, that means no one else will give solution, so don't waste time
    solved, noOfNodesChecked, totalTime, manhattenHeuristicNodesVisited, level, parentMD = ManhattanDistanceHeuristic.manhattenHeuristic(start)
    print("ManhattanDistanceHeuristic - ", solved, noOfNodesChecked, totalTime, level)
    # if solved == "YES":
    #     solved, noOfNodesChecked, totalTime, misplacedHeuristicNodesVisited, level, parentMT = MisplacedTileHeuristic.misplacedHeuristic(start)
    #     print("MisplacedTileHeuristic - ", solved, noOfNodesChecked, totalTime, level)
    #     solved, noOfNodesChecked, totalTime, zeroHeuristicNodesVisited, level, parentZH = ZeroHeuristic.zeroHeuristic(start)
    #     print("ZeroHeuristic - ", solved, noOfNodesChecked, totalTime, level)
    #     solved, noOfNodesChecked, totalTime, incorrectHeuristicNodesVisited, level, parentIH = IncorrectHeuristic.incorrectHeuristic(start)
    #     print("IncorrectHeuristic - ", solved, noOfNodesChecked, totalTime, level)
    #     print("-----------------------------------------------------------------")
    #     print("Number of elements matched between h(n) = manhatten distance and h(n) = misplaced tile - ", util.noOfElementsMatched(misplacedHeuristicNodesVisited, manhattenHeuristicNodesVisited))
    #     print("Length of nodes Visited, for h(n) = manhatten distance - ", len(misplacedHeuristicNodesVisited), "for h(n) = misplaced - ",  len(manhattenHeuristicNodesVisited), "\n")
    #     print("-----------------------------------------------------------------")
    #     print("Number of elements matched between h(n) = manhatten distance and h(n) = zero - ", util.noOfElementsMatched(manhattenHeuristicNodesVisited, zeroHeuristicNodesVisited))
    #     print("Length of nodes Visited, for h(n) = manhatten distance - ", len(manhattenHeuristicNodesVisited), "for h(n) = misplaced - ",  len(zeroHeuristicNodesVisited), "\n")
    #     print("-----------------------------------------------------------------")
    #     print("Number of elements matched between h(n) = misplaced and h(n) = zero - ", util.noOfElementsMatched(misplacedHeuristicNodesVisited, zeroHeuristicNodesVisited))
    #     print("Length of nodes Visited, for h(n) = manhatten distance - ", len(misplacedHeuristicNodesVisited), "for h(n) = misplaced - ",  len(zeroHeuristicNodesVisited), "\n")
    #     print("-----------------------------------------------------------------")
    #     print("Number of elements matched between h(n) = manhatten distance and h(n) = sub-optimal - ", util.noOfElementsMatched(manhattenHeuristicNodesVisited, incorrectHeuristicNodesVisited))
    #     print("Length of nodes Visited, for h(n) = manhatten distance - ", len(manhattenHeuristicNodesVisited), "for h(n) = sub-optimal - ", len(incorrectHeuristicNodesVisited))
    #     print("-----------------------------------------------------------------")
    #     inp = input("Do you want to see path to Goal for Manhatten Distance(Y/N)")
    #     if inp == "Y":
    #         parentMD.reverse()
    #         print(parentMD)
    #     print("-----------------------------------------------------------------")
    #     inp = input("Do you want to see path to Goal for Misplaced Tile(Y/N)")
    #     if inp == "Y":
    #         parentMT.reverse()
    #         print(parentMT)
    #     print("-----------------------------------------------------------------")
    #     inp = input("Do you want to see path to Goal for Zero Heuristic(Y/N)")
    #     if inp == "Y":
    #         parentZH.reverse()
    #         print(parentZH)
    #     print("-----------------------------------------------------------------")
    #     inp = input("Do you want to see path to Goal for Sub Optimal(Y/N)")
    #     if inp == "Y":
    #         parentIH.reverse()
    #         print(parentIH)
    #     print("-----------------------------------------------------------------")
    # else:
    #     print("NO SOLUTION FOUND")
