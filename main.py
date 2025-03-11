import ast
import heapq
import logging
import sys

import numpy as np

import visualize

logging.basicConfig(level=logging.INFO)


def update_paths(dest, g, open_list, new_x, new_y, cell_details, parent_pos):
    """
    Updates the open list and cell details based on the new cell to be evaluated.

    Parameters
    ----------
    dest : tuple
        The destination coordinates (x, y)
    g : int
        The cost of the path from the start to the current cell
    open_list : list
        The list of cells to be evaluated, sorted by total cost
    new_x : int
        The x-coordinate of the new cell
    new_y : int
        The y-coordinate of the new cell
    cell_details : dict
        The dictionary of cell details, where each key is a cell and the value is
        a dictionary with the keys 'total cost', 'g', 'h', and 'parent'
    parent_pos : tuple
        The coordinates of the parent cell
    """
    pos_cell = (new_x, new_y)

    # Updating Values
    new_g = g + 1  # Increment g to reflect the step cost from the parent
    h = abs(new_x - dest[0]) + abs(new_y - dest[1])
    final_cost = new_g + h

    # Checking if we've seen this node before with less cost
    if (
        pos_cell not in cell_details
        or cell_details[pos_cell]["total cost"] > final_cost
    ):
        heapq.heappush(open_list, (final_cost, new_g, pos_cell))
        cell_details[(new_x, new_y)] = {}
        cell_details[pos_cell]["total cost"] = final_cost
        cell_details[pos_cell]["g"] = new_g
        cell_details[pos_cell]["h"] = h
        cell_details[pos_cell]["parent"] = parent_pos  # replacing previous parent


def a_star_search(maze, src, dest):
    """
    Implements the A* pathfinding algorithm to find the shortest path from a start position to a destination position in a maze.

    Parameters
    ----------
    maze : 2D list
        The 2D list representing the maze, where 0s represent passable cells and 1s represent blocked cells
    src : tuple
        The coordinates of the start position (x, y)
    dest : tuple
        The coordinates of the destination position (x, y)

    Returns
    -------
    tuple
        A tuple containing the path (a list of coordinates from destination to source), the open list (a list of cells to be evaluated), the closed list (a set of visited cells), and the cell details (a dictionary of cell details, where each key is a cell and the value is a dictionary with the keys 'total cost', 'g', 'h', and 'parent')
    """
    # Initializing cost values
    g = 0  # Cost from start (G: cost)

    # Manhattan distance (H: heuristic)
    h = abs(src[0] - dest[0]) + abs(src[1] - dest[1])
    total_cost = g + h

    # Initialize the open list (cells to be visited) with the start cell
    open_list = [(total_cost, g, src)]
    heapq.heapify(open_list)

    # Initialize the closed list (visited cells) and cell details
    closed_list = set()
    cell_details = {src: {"total cost": total_cost, "g": g, "h": h, "parent": src}}

    # Possible directions of movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(open_list) > 0:
        # Pop the cell with the lowest total cost
        total_cost, g, current_pos = heapq.heappop(open_list)
        closed_list.add(current_pos)

        x, y = current_pos

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if not (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0])):
                continue

            cell_value = maze[new_x][new_y]
            pos_cell = (new_x, new_y)

            if cell_value == 0:
                # Skip blocked cells
                logging.debug("Blocked cell")
                continue

            if pos_cell in closed_list:
                # Skip already visited nodes
                logging.info("Already visited node")
                continue

            # Update paths and cell details
            update_paths(dest, g, open_list, new_x, new_y, cell_details, current_pos)

            # Check if the destination is reached
            if pos_cell == dest:
                logging.info("The destination cell is found")

                # Reconstruct the path from destination to source
                path_list = [pos_cell]
                child = pos_cell

                while child != src:
                    path_list.append(cell_details[child]["parent"])
                    child = cell_details[child]["parent"]

                return path_list, open_list, closed_list, cell_details

    logging.info("No path found")
    return None, open_list, closed_list, cell_details


def input_handler():
    """
    Handles input from the user.
    Asks the user whether they want to enter their own maze or not.

    Returns:
        maze (numpy array): 2D array representing the maze
        src (tuple): (x, y) coordinates of the starting point
        dest (tuple): (x, y) coordinates of the destination point
    """
    mode = input("Do you want to enter the maze?(yes/no) ")
    if mode == "yes":
        print("Enter the maze in a matrix form (0 for blocked, 1 for unblocked)")
        print("Press  Enter + Ctrl+D (Linux/macOS) or Ctrl+Z (Windows)  to finish")
        maze = sys.stdin.read()
        maze = np.array(ast.literal_eval(maze))
        ROW, COL = maze.shape
    else:
        ROW = int(input("How many rows do you want in your maze?"))
        COL = int(input("How many columns do you want in your maze?"))
        maze = np.random.choice([0, 1], size=(ROW, COL))

    src = ast.literal_eval(input("Enter the starting point : "))
    dest = ast.literal_eval(input("Enter the destination point : "))
    return maze, src, dest


if __name__ == "__main__":

    maze, src, dest = input_handler()
    path_list, open_list, closed_list, cell_details = a_star_search(maze, src, dest)

    if path_list is None:
        logging.info("No path found")
    else:
        print("The Optimal Path is")
        print("->".join(map(str, path_list)))

    visualize.main(maze, src, dest, path_list, maze.shape)
