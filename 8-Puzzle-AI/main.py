# Entry point للمشروع
# الهدف منه تشغيل Algorithm واحد بشكل بسيط للتجربة

from Puzzle.State import State
from Algorithms.BFS import solve as bfs_solve


def main():
    # تعريف الحالة الابتدائية
    initial_state = State(
        board=[1, 2, 3,
               4, 0, 5,
               6, 7, 8]
    )

    # تشغيل BFS كتجربة
    result = bfs_solve(initial_state)

    solution = result["solution"]
    metrics = result["metrics"]

    if solution:
        print("Solution Found!")
        print("Path Cost:", solution.cost)
        print("Nodes Expanded:", metrics.nodes_expanded)
        print("Time Taken:", round(metrics.time_taken, 4), "seconds")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
