# hill_climbing.py
# Hill Climbing Algorithm for the 8-Puzzle problem

from Puzzle.Puzzle import is_goal, get_successors
from Puzzle.State import State
from Utils.Heuristics import manhattan_distance
from Utils.Metrics import Metrics


def solve(initial_state):
    """
    Hill Climbing Algorithm

    initial_state : State object
    return        : dictionary يحتوي على الحل (إن وجد) و الـ metrics
    """

    # نبدأ تسجيل الأداء
    metrics = Metrics()

    # نبدأ من الحالة الابتدائية
    current_state = initial_state

    while True:
        # بنحسب node expanded
        metrics.nodes_expanded += 1

        # لو وصلنا للهدف
        if is_goal(current_state):
            metrics.stop()
            return {
                "solution": current_state,
                "metrics": metrics
            }

        # نطلع كل الجيران (الحالات الممكنة)
        neighbors = []

        for next_board in get_successors(current_state):
            next_state = State(
                board=next_board,
                parent=current_state,
                move=None,
                depth=current_state.depth + 1,
                cost=current_state.cost + 1
            )
            neighbors.append(next_state)

        # نحسب heuristic للحالة الحالية
        current_h = manhattan_distance(current_state.board)

        # نختار أحسن Neighbor (أقل heuristic)
        best_neighbor = None
        best_h = current_h

        for neighbor in neighbors:
            h = manhattan_distance(neighbor.board)
            if h < best_h:
                best_h = h
                best_neighbor = neighbor

        # لو ملقيناش Neighbor أحسن → نقف (Local Optimum)
        if best_neighbor is None:
            metrics.stop()
            return {
                "solution": current_state,   # الحل الحالي (مش optimal غالبًا)
                "metrics": metrics
            }

        # نتحرك لأحسن Neighbor
        current_state = best_neighbor
