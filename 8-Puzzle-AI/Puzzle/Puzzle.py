# هذا الملف يحتوي على منطق لعبة 8- Puzzle فقط

# الحالة النهائية اللي كل الخوارزميات بتحاول توصل لها
GOAL_STATE = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]   # 0 يمثل المكان الفاضي


def is_goal(state):
    """
    تتحقق هل الحالة الحالية هي حالة الهدف ولا لا
    
    state : كائن من نوع State
    return: True لو وصلنا للحل، False غير كده
    """
    return state.board == GOAL_STATE


def get_successors(state):
    """
    ترجع كل الحالات الممكنة اللي نقدر ننتقل لها
    من الحالة الحالية عن طريق تحريك المكان الفاضي (0)
     
    state : الحالة الحالية
    return: list of boards (حالات جديدة)
    """

    successors = []

    # البورد الحالي
    board = state.board

    # مكان الـ 0 في البورد
    zero_index = board.index(0)

    # نحسب الصف والعمود في Grid 3x3
    row, col = divmod(zero_index, 3)

    def swap(i, j):
        """
        دالة مساعدة:
        تبدّل مكان عنصرين في البورد
        وترجع بورد جديد (من غير ما نعدل الأصلي)
        """
        new_board = board.copy()
        new_board[i], new_board[j] = new_board[j], new_board[i]
        return new_board

    # تحريك الـ 0 لفوق
    if row > 0:
        successors.append(swap(zero_index, zero_index - 3))

    # تحريك الـ 0 لتحت
    if row < 2:
        successors.append(swap(zero_index, zero_index + 3))

    # تحريك الـ 0 شمال
    if col > 0:
        successors.append(swap(zero_index, zero_index - 1))

    # تحريك الـ 0 يمين
    if col < 2:
        successors.append(swap(zero_index, zero_index + 1))

    return successors
