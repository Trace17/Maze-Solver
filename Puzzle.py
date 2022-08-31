# Name: Trace Sweeney
# OSU Email: Sweenetr@oregonstate.edu
# Course: CS325 - Analysis of Algorithms 
# Assignment: 6
# Due Date: Aug 1, 2022
# Description: This assignment implements a breadth first search from a source spot, to find
# a destination spot within a puzzle. This program works as a maze searcher.

def solve_puzzle(Board, Source, Destination):
    """This function implements a breadth first search from a source spot finding a destination
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
    """
    distance_map = [[-1] * len(Board[0]) for _ in range(len(Board))] #create the map
    directions = "" #create the directions string
    left = -1       #left movement
    right = 1       #right movement
    up = -1         #upward movement
    down = 1        #downward movement
    queue = []      #an empty queue
    visited = []    #an empty list to track which spots have already been visited
    source_spot = [Source[0], Source[1]]      #creating a list from the source tuple
    current_spot = source_spot                #setting the current spot to the source
    destination_spot = [Destination[0], Destination[1]]   #creating a list from the destination tuple
    distance_map[current_spot[0]][current_spot[1]] = 0
    queue.append([current_spot[0],current_spot[1]])
    solution = []
    #we want to start from the node and then check all nodes surrounding it. 
    while distance_map[destination_spot[0]][destination_spot[1]] == -1 and len(queue) > 0:
        #check all nodes around the current_node and add them to a queue
        visited.append(current_spot)
        #upward validation
        if current_spot[0] != 0 and Board[current_spot[0] + up][current_spot[1]] != "#" and [current_spot[0] + up, current_spot[1]] not in visited:
            queue.append([current_spot[0] + up, current_spot[1]])
            distance_map[current_spot[0] + up][current_spot[1]] = distance_map[current_spot[0]][current_spot[1]] + 1
        #downward validation
        if current_spot[0] != len(Board)-1 and Board[current_spot[0] + down][current_spot[1]] != "#" and [current_spot[0] + down, current_spot[1]] not in visited:
            queue.append([current_spot[0] + down, current_spot[1]]) 
            distance_map[current_spot[0] + down][current_spot[1]] = distance_map[current_spot[0]][current_spot[1]] + 1
        #left validation
        if current_spot[1] != 0 and Board[current_spot[0]][current_spot[1] + left] != "#" and [current_spot[0], current_spot[1] + left] not in visited:
            queue.append([current_spot[0], current_spot[1] + left]) 
            distance_map[current_spot[0]][current_spot[1] + left] = distance_map[current_spot[0]][current_spot[1]] + 1
        #right validation
        if current_spot[1] != len(Board[0])-1 and Board[current_spot[0]][current_spot[1] + right] != "#" and [current_spot[0], current_spot[1] + right] not in visited:
            queue.append([current_spot[0], current_spot[1] + right]) 
            distance_map[current_spot[0]][current_spot[1] + right] = distance_map[current_spot[0]][current_spot[1]] + 1
        queue.pop(0) #deque 
        #check to see if the queue is empty. This means the value cannot be reached or was not found
        if len(queue) == 0: 
            return None
        current_spot = queue[0]

    #Destination reached, walk back to original spot and add locations to solution
    min_value = distance_map[destination_spot[0]][destination_spot[1]]
    current_spot = destination_spot
    solution_column_spot = current_spot[0]
    solution_row_spot = current_spot[1]
    solution.append((solution_column_spot, solution_row_spot))
    letter = ""
    while current_spot != source_spot:
        #check all nodes around the current_node for the smallest value greater than 0
        #upward validation
        if current_spot[0] != 0 and distance_map[current_spot[0] + up][current_spot[1]] >= 0 and distance_map[current_spot[0] + up][current_spot[1]] < min_value:
            min_value = distance_map[current_spot[0] + up][current_spot[1]]
            solution_column_spot = current_spot[0] + up
            letter = "D"
        #downward validation
        if current_spot[0] != len(Board)-1 and distance_map[current_spot[0] + down][current_spot[1]] >= 0 and distance_map[current_spot[0] + down][current_spot[1]] < min_value:
            min_value = distance_map[current_spot[0] + down][current_spot[1]]
            solution_column_spot = current_spot[0] + down
            letter = "U"
        #left validation
        if current_spot[1] != 0 and distance_map[current_spot[0]][current_spot[1] + left] >= 0 and distance_map[current_spot[0]][current_spot[1] + left] < min_value:
            min_value = distance_map[current_spot[0]][current_spot[1] + left]
            solution_row_spot = current_spot[1] + left
            letter = "R"
        #right validation
        if current_spot[1] != len(Board[0])-1 and distance_map[current_spot[0]][current_spot[1] + right] >= 0 and distance_map[current_spot[0]][current_spot[1] + right] < min_value:
            min_value = distance_map[current_spot[0]][current_spot[1] + right]
            solution_row_spot = current_spot[1] + right
            letter = "L"
        directions += letter #add the letter to the directions
        current_spot = [solution_column_spot, solution_row_spot] #update the current spot
        solution.append((solution_column_spot, solution_row_spot)) #append the tuple of directions to solution
    reversed_directions = directions[::-1] #reverse the directions string 
    solution.reverse() #reverse the solution string
    solution_with_directions = (solution, reversed_directions) #create our return tuple
    return solution_with_directions

Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '-', '-', '-'],
    ['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0,2), (2,2)))
print(solve_puzzle(Puzzle, (0,0), (4,4)))
print(solve_puzzle(Puzzle, (0,0), (4,0)))