from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics

def depth_limited_search(state, limit, metrics, visited):
    """
    A helper function that performs Depth-Limited Search (DLS).
    It explores nodes up to a specific depth 'limit'.
    """
    # Goal Check
    if Puzzle.is_goal(state):
        return state
    
    # If the depth limit is reached, stop exploring this branch
    if limit <= 0:
        return None
    
    metrics.nodes_expanded += 1
    
    # Explore neighbors
    for next_board in Puzzle.get_successors(state):
        successor_state = State.State(
            board=next_board, 
            parent=state, 
            depth=state.depth + 1,
            cost=state.cost + 1
        )
        
        # Recursive call with decremented limit
        result = depth_limited_search(successor_state, limit - 1, metrics, visited)
        
        # If a solution is found in the deeper layers, propagate it up
        if result is not None:
            return result
            
    return None

def solve(initial_board):
    """
    Solves the 8-Puzzle using Iterative Deepening Search (IDS).
    IDS repeatedly applies DLS with increasing limits (0, 1, 2, ...).
    """
    metrics = Metrics.Metrics()
    initial_state = State.State(board=initial_board, depth=0, cost=0)
    
    # Iteratively increase the depth limit
    # Max depth set to 50 as 8-puzzle solutions rarely exceed 31 moves
    for limit in range(50):
        # In IDS, we usually clear visited for each depth to ensure optimality
        # but the depth limit itself prevents infinite recursion.
        result_state = depth_limited_search(initial_state, limit, metrics, set())
        
        # If solution found at current limit, return it
        if result_state is not None:
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(result_state)
            return {"solution": solution_path, "metrics": metrics}
            
    # If the loop finishes without finding a solution
    metrics.stop()
    return {"solution": None, "metrics": metrics}
