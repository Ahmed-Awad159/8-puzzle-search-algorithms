# دا مثال لاستخدام اول الجوريزم اهو وباستخدام الفانكشنز الثابته واللي المفروض نستخدمها ومنعملش فانكشن خاصه بكل واحد
# Breadth-First Search Algorithm for 8-Puzzle

from collections import deque
from Puzzle.Puzzle import is_goal, get_successors
from Puzzle.State import State
from Utils.Metrics import Metrics


def solve(initial_state):
    """
    BFS Algorithm
    
    initial_state : State object
    return : dictionary يحتوي على الحل و الـ metrics
    """

    # نبدأ تسجيل الأداء
    metrics = Metrics()

    # Queue علشان BFS
    queue = deque()
    queue.append(initial_state)

    # states اللي زرناها قبل كده
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()

        # بنحسب node expanded
        metrics.nodes_expanded += 1

        # لو وصلنا للهدف
        if is_goal(current_state):
            metrics.stop()
            return {
                "solution": current_state,
                "metrics": metrics
            }

        # نوسّع العقدة الحالية
        for next_board in get_successors(current_state):
            next_state = State(
                board=next_board,
                parent=current_state,
                move=None,                   # الحركة ممكن نحددها لاحقًا
                depth=current_state.depth + 1,
                cost=current_state.cost + 1
            )

            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    # لو مفيش حل
    metrics.stop()
    return {
        "solution": None,
        "metrics": metrics
    }
