# Creating a class to keep grid and its relevant data
class Node:
    def __init__(self, parent, grid, emptyTile):
        self.parent = parent
        self.grid = grid
        self.emptyTile = emptyTile
