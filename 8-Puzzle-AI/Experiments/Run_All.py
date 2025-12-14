# الملف ده مسؤول عن تشغيل كل Algorithms مرة واحدة
# وتجميع نتائج الأداء (time, nodes expanded, etc.)

# استيراد كل الخوارزميات
# كل Algorithm لازم يكون فيه دالة اسمها solve()
from Algorithms import BFS, DFS, UCS, IDS, A_Star, Hill_Climbing
from Puzzle.State import State


# الحالة الابتدائية اللي هنختبر عليها كل الخوارزميات
initial_state = State(
    board=[1, 2, 3,
           4, 0, 5,
           6, 7, 8]
)

# Dictionary بيربط اسم الخوارزمية بالدالة اللي بتشغّلها
ALGORITHMS = {
    "BFS": BFS.solve,
    "DFS": DFS.solve,
    "UCS": UCS.solve,
    "IDS": IDS.solve,
    "A*": A_Star.solve,
    "Hill Climbing": Hill_Climbing.solve,
}

# تشغيل كل Algorithm واحدة واحدة
for name, algo in ALGORITHMS.items():
    print(f"\nRunning {name} ...")

    # تشغيل الخوارزمية
    result = algo(initial_state)

    # استخراج الـ metrics
    metrics = result["metrics"]

    # طباعة النتائج الأساسية
    print(f"Time Taken      : {metrics.time_taken:.4f} seconds")
    print(f"Nodes Expanded  : {metrics.nodes_expanded}")
