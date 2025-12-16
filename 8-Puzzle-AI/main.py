# main.py
# Test Hill Climbing algorithm on the 8-Puzzle problem

from Puzzle.State import State
from Algorithms.Hill_Climbing import solve as hill_climbing_solve


def test_algorithm(name, solve_func, initial_state):
    print(f"\nRunning {name}...")
    result = solve_func(initial_state)

    solution = result["solution"]
    metrics = result["metrics"]

    if solution is None:
        print("No solution found.")
    else:
        print("Result state reached:")
        print(solution.board)
        print("Path Cost       :", solution.cost)
        print("Nodes Expanded  :", metrics.nodes_expanded)
        print("Time Taken (ms):", round(metrics.time_taken, 2))



if __name__ == '__main__':

    # Initial state (solvable)
    initial_state = State(
        board=[8, 4, 6,
               2, 0, 1,
               3, 7, 5]
    )

    print("===== Hill Climbing Test =====")
    test_algorithm("Hill Climbing", hill_climbing_solve, initial_state)
