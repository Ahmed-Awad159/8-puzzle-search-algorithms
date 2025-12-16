# astar.py
# A* Search Algorithm for the 8-Puzzle problem

import heapq
from Puzzle.Puzzle import is_goal, get_successors
from Puzzle.State import State
from Utils.Heuristics import manhattan_distance
from Utils.Metrics import Metrics


def solve(initial_state):
    """
    A* Search Algorithm

    initial_state : State object (initial configuration of the puzzle)
    return        : dictionary containing the solution and performance metrics
    """

    # نبدأ تسجيل الأداء
    metrics = Metrics()

    # Priority Queue (Min-Heap)
    # كل عنصر فيها بالشكل:
    # (f_cost, counter, state)
    # counter لتجنب مشاكل المقارنة بين الـ State objects
    open_list = []
    counter = 0

    # نحسب f = g + h للحالة الابتدائية
    start_h = manhattan_distance(initial_state.board)
    heapq.heappush(open_list, (start_h, counter, initial_state))

    # states اللي زرناها قبل كده
    visited = set()

    while open_list:
        # نطلع الحالة اللي أقل f-cost
        _, _, current_state = heapq.heappop(open_list)

        # لو الحالة اتزارت قبل كده نعدّيها
        if current_state in visited:
            continue

        visited.add(current_state)

        # بنحسب node expanded
        metrics.nodes_expanded += 1

        # لو وصلنا للهدف
        if is_goal(current_state):
            metrics.stop()
            return {
                "solution": current_state,
                "metrics": metrics
            }

        # نوسع العقدة الحالية
        for next_board in get_successors(current_state):
            next_state = State(
                board=next_board,
                parent=current_state,
                move=None,                       # الحركة ممكن تتحدد لاحقًا
                depth=current_state.depth + 1,
                cost=current_state.cost + 1      # g(n)
            )

            if next_state not in visited:
                # نحسب h(n)
                h = manhattan_distance(next_state.board)

                # f(n) = g(n) + h(n)
                f = next_state.cost + h

                counter += 1
                heapq.heappush(open_list, (f, counter, next_state))

    # لو مفيش حل
    metrics.stop()
    return {
        "solution": None,
        "metrics": metrics
    }
