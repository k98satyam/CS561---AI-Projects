import NodeStructure
import util
import BFS
import DFS

if __name__ == '__main__':
    # randonGrid, randomRow, randomCol = util.generateRandomGrid()
    explored = {tuple(tuple(row) for row in [[2, 5, 3], [4, 8, 1], [7, 0, 6]]): 1}
    start = NodeStructure.Node(None, [[2, 5, 3], [4, 8, 1], [7, 0, 6]], [2, 1])
    print("Initial Grid Configuration-")
    for configGrid in [[2, 5, 3], [4, 8, 1], [7, 0, 6]]:
        print(configGrid)
    print("Goal Grid Configuration-")
    for goalRow in [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        print(goalRow)
    solutionFoundBFS, noOfNodesCheckedBFS, bfsTime, parentListBFS, allNodesVisitedBFS = BFS.BFS(start)
    solutionFoundDFS, noOfNodesCheckedDFS, dfsTime, parentListDFS, allNodesVisitedDFS = DFS.DFS(start)
    print("Order In which nodes are generated - UP, DOWN, RIGHT, LEFT")
    print("BFS-")
    print("Solution Found- ", solutionFoundBFS, "No. Of Nodes Searched- ", noOfNodesCheckedBFS)
    print("DFS-")
    print("Solution Found- ", solutionFoundDFS, "No. Of Nodes Searched- ", noOfNodesCheckedDFS)
    print("Time Taken(in seconds), For BFS - ", bfsTime, ",For DFS - ", dfsTime)
    # if solutionFoundBFS == "YES" and solutionFoundDFS == "YES" and input("Do You want to see all the nodes Visited? (Y/N)") == 'Y':
    #     print("DFS")
    #     for i in allNodesVisitedDFS:
    #         print(i)
    #     print("DFS")
    #     for i in allNodesVisitedDFS:
    #         print(i)
    # if solutionFoundBFS == "YES" and solutionFoundDFS == "YES" and input("Do You want to see all the parent nodes of Goal State? (Y/N)") == 'Y':
    #     print("Path BFS-")
    #     for i in parentListBFS:
    #         print(i)
    #     print("Path DFS-")
    #     for i in parentListDFS:
    #         print(i)
