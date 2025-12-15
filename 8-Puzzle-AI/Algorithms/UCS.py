import heapq
from Puzzle import Puzzle  # Corrected import: Assumes Puzzle.py defines functions directly
from Puzzle import State   # Corrected import: Assumes State.py defines the State class
from Utils import Metrics # Corrected import: Assumes Metrics.py defines the Metrics class
import math # Used for setting initial infinite cost


# --- UCS Algorithm ---
def solve_8_puzzle_ucs(initial_board):
    """
    Solves the 8-Puzzle using Uniform Cost Search (UCS).
    Uses a Priority Queue (Min-Heap) to always expand the node with the lowest cost (g(n)).
    """
    print("--- Starting 8-Puzzle UCS Solver ---")

    # Initialize Metrics tracking (Assumes Metrics.py contains the Metrics class)
    metrics = Metrics.Metrics()
    
    # 1. Initialization
    initial_state = State.State(board=initial_board, depth=0, cost=0)
    
    # FIX for TypeError: '<' not supported (Tie-breaker counter)
    tie_breaker = 0 
    
    # Priority Queue: Stores (cost, tie_breaker, State object)
    priority_queue = [(0, tie_breaker, initial_state)]
    
    # cost_to_reach: Dictionary to track the lowest cost found *so far* to reach any state.
    cost_to_reach = {initial_state: 0} 

    # 2. Loop
    while priority_queue:
        
        # FIX for TypeError: heappop now correctly unpacks the tie-breaker element
        cost, _, current_state = heapq.heappop(priority_queue)
        metrics.nodes_expanded += 1
        
        # Check if the path pulled from the queue is worse than a known, cheaper path.
        if cost > cost_to_reach.get(current_state, math.inf):
            continue
            
        # 2.1. Goal Check
        if Puzzle.is_goal(current_state):
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(current_state)
            
            # Print the solution steps
            print("\n" + "="*40)
            print(f"✨ SOLUTION FOUND! (Total moves: {len(solution_path) - 1})")
            print("="*40)
            for i, board in enumerate(solution_path):
                print(f"➡️ Step {i}:")
                Puzzle.print_puzzle(board)

            return {"solution": solution_path, "metrics": metrics}

        # 2.2. Generate and Explore Neighbors
        for next_board in Puzzle.get_successors(current_state):
            
            # FIX for 'cannot access local variable new_cost' (Calculation must be inside the loop)
            step_cost = 1 
            new_cost = current_state.cost + step_cost
            
            # Check if this new path is shorter (cheaper) than any previously found path
            if new_cost < cost_to_reach.get(State.State(board=next_board), math.inf):
                
                # Update the best known cost to reach the neighbor
                cost_to_reach[State.State(board=next_board)] = new_cost
                
                # Create the new state node
                neighbor_state = State.State(
                    board=next_board, 
                    parent=current_state, 
                    depth=current_state.depth + 1,
                    cost=new_cost # Store the total accumulated cost (g(n))
                )
                
                # FIX for TypeError: heappush now includes the tie-breaker
                tie_breaker += 1
                heapq.heappush(priority_queue, (new_cost, tie_breaker, neighbor_state))
                
    # If the queue empties and the goal is not reached (e.g., unsolvable state)
    metrics.stop()
    print("No solution found (Puzzle may be unsolvable).")
    return {"solution": None, "metrics": metrics}
