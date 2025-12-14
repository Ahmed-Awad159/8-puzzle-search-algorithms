# هذا الملف يحتوي على دوال Heuristic تُستخدم مع
# الملف دا يستخدمه اللي هيشتغل علي A* و Hill Climbing


def misplaced_tiles(board):
    """
    Misplaced Tiles Heuristic
    
    بتحسب عدد البلاطات اللي مش في مكانها الصحيح
    (ماعدا البلاطة الفاضية 0)

    board : list تمثل حالة البازل الحالية
    return: عدد البلاطات الغلط
    """
    count = 0

    for i in range(9):
        # نتجاهل البلاطة الفاضية
        if board[i] != 0 and board[i] != i + 1:
            count += 1

    return count


def manhattan_distance(board):
    """
    Manhattan Distance Heuristic
    
    بتحسب مجموع المسافات الأفقية والرأسية
    لكل بلاطة من مكانها الحالي لمكانها الصحيح

    board : list تمثل حالة البازل الحالية
    return: مجموع المسافات (قيمة heuristic)
    """
    distance = 0

    for i in range(9):
        # نتجاهل البلاطة الفاضية
        if board[i] != 0:
            # المكان الصحيح للبلاطة
            goal_pos = board[i] - 1

            # نحسب المسافة بين المكان الحالي والمكان الصحيح
            distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)

    return distance
