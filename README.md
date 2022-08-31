# Maze-Solver
    This function implements a breadth first search from a source spot finding a destination
    spot within a puzzle. It does this by creating a map with values corresponding to distances
    to a spot on the map and traces these distances back to find the shortest path.
    Input: 
    1. A board representing a puzzle with "-"s as spots that can be traversed and "#"s 
    for spots that cannot. 
    2. A source spot on the board as a tuple
    3. A destination spot on the board as a tuple
    Output:
    A tuple containing
    1. A list of the shortest path coordinates from the source to the destination
    2. A string of letters (L,R,U,D) representing Left, right, up, and down coordinates
    corresponding to the coordinates for the shortest path.
    
## How to use

    To use this program, copy the file "Puzzle.py" and scroll to the bottom of the file to change the puzzle and then run the command 
    "print(solve_puzzle(Puzzle, (0,2), (2,2)))" change the coordinates for start (0,2) in the example and end (2,2) as you would like!
    There are three example cases at the bottom of the file which you can play around with!
