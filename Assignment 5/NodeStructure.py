# Creating a class to keep grid and its relevant data
class Node:
    def __init__(self, parent, grid, emptyTile, costTillNow):
        self.parent = parent
        self.grid = grid
        self.emptyTile = emptyTile
        self.costTillNow = costTillNow  # This holds our f(n) = g(n) + h(n), where g(n) = cost so far, and h(n) = heuristic function

    def __lt__(self, other):
        return self.costTillNow < other.costTillNow
