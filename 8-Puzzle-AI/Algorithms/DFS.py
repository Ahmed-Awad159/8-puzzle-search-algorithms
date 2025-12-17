import collections
from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics

def solve(initial_board):
    """
    Solves the 8-Puzzle using Depth-First Search (DFS).
    DFS explores as far as possible along each branch before backtracking.
    """
    # Initialize Metrics tracking
    metrics = Metrics.Metrics()
    
    # Create the initial state object
    initial_state = State.State(board=initial_board, depth=0, cost=0)

    # Stack (Frontier): DFS uses LIFO (Last-In, First-Out)
    # Using a list as a stack
    stack = [initial_state]
    
    # Visited Set: To keep track of explored states and prevent infinite loops (cycles)
    visited = {tuple(initial_state.board)} 

    # Start the search loop
    while stack:
        # Pop the last added state (deepest node)
        current_state = stack.pop()
        metrics.nodes_expanded += 1

        # Goal Check: Check if the current state matches the goal configuration
        if Puzzle.is_goal(current_state):
            metrics.stop()
            # Trace back the path from goal to start
            solution_path = Puzzle.reconstruct_path(current_state)
            return {"solution": solution_path, "metrics": metrics}

        # Generate and Explore Neighbors
        # Reversed is used to maintain consistent exploration order with BFS
        for next_board in reversed(Puzzle.get_successors(current_state)):
            
            # Create a new State object for each successor
            successor_state = State.State(
                board=next_board, 
                parent=current_state, 
                depth=current_state.depth + 1,
                cost=current_state.cost + 1
            )

            # Check if the board configuration has been visited before
            board_tuple = tuple(successor_state.board)
            if board_tuple not in visited:
                visited.add(board_tuple)
                stack.append(successor_state)
                
    # If no solution is found
    metrics.stop()
    return {"solution": None, "metrics": metrics}
