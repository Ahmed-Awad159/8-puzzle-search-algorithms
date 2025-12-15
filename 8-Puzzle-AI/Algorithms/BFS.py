import collections
from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics
# Note: You should ensure State.py, Puzzle.py, and Metrics.py are in the same directory, 
# or properly imported via the Python path.



def solve(initial_board):
    """
    Solves the 8-Puzzle using Breadth-First Search (BFS).

    Args:
        initial_board (list): The starting 8-puzzle configuration (list of 9 integers).

    Returns:
        dict: A dictionary containing the solution path (list of states) and performance metrics.
    """

    # Initialize Metrics tracking
    metrics = Metrics.Metrics()
    
    # 1. Initialization
    initial_state = State.State(board=initial_board, depth=0, cost=0)

    # Queue (Frontier): Stores State objects to be explored. BFS uses FIFO.
    queue = collections.deque([initial_state])
    
    # Visited Set: Stores State objects (or just the board tuple hash) to prevent cycles.
    # Using the State object itself works because __hash__ and __eq__ are defined.
    visited = {initial_state} 

    # 2. Loop
    while queue:
        # Dequeue the state with the highest priority (lowest depth/cost)
        current_state = queue.popleft()
        metrics.nodes_expanded += 1

        # 2.1. Goal Check
        if Puzzle.is_goal(current_state):
            metrics.stop()
            # Reconstruct the path from the goal state back to the initial state
            solution_path = Puzzle.reconstruct_path(current_state)

            # --- Printing Every Step ---
            print("\n" + "="*40)
            print(f"✨ SOLUTION FOUND! (Total moves: {len(solution_path) - 1})")
            print("="*40)
            
            # Loop through the solution path (list of boards) and print each one
            for i, board in enumerate(solution_path):
                print(f"➡️ Step {i}:")
                Puzzle.print_puzzle(board)
            # --- End Printing ---

            return {"solution": solution_path, "metrics": metrics}

        # 2.2. Generate and Explore Neighbors
        # successors returns a list of board lists (e.g., [[1, 2, 3, ...]])
        for next_board in Puzzle.get_successors(current_state):
            
            # Create a new State object for the successor
            # Cost is the current cost + 1 (since all moves cost 1)
            # Depth increases by 1
            successor_state = State.State(
                board=next_board, 
                parent=current_state, 
                move=None, # The move info can be deduced by comparing current_state and next_board
                depth=current_state.depth + 1,
                cost=current_state.cost + 1
            )

            # Check if this new state has been visited
            if successor_state not in visited:
                visited.add(successor_state)
                queue.append(successor_state)
                
    # If the queue empties and the goal is not reached (e.g., unsolvable state)
    metrics.stop()
    return {"solution": None, "metrics": metrics}



