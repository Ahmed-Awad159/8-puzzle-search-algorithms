# هذا الملف بيمثل "State" واحدة في مشكلة 8-Puzzle
# أي حالة = شكل البازل في لحظة معينة أثناء البحث

class State: # بيمثل حالة في - Puzzle
    def __init__(self, board, parent=None, move=None, depth=0, cost=0): 
        """
        Constructor لإنشاء حالة جديدة
        
        board  : شكل البازل الحالي (list من 9 عناصر)
        parent : الحالة السابقة اللي جينا منها (مهم لإعادة بناء الحل)
        move   : الحركة اللي اتعملت للوصول للحالة دي (Up, Down, Left, Right)
        depth  : عدد الحركات من البداية لحد الحالة الحالية
        cost   : تكلفة الوصول للحالة (في 8-Puzzle كل حركة = 1)
        """
        self.board = board        # شكل البازل الحالي
        self.parent = parent      # Reference للحالة السابقة
        self.move = move          # الحركة اللي أدت للحالة دي
        self.depth = depth        # العمق في شجرة البحث
        self.cost = cost          # تكلفة المسار حتى هذه الحالة

    def __eq__(self, other): 
        """
        بتحدد إمتى حالتين يعتبروا متساويين
        حالتين متساويين لو ترتيب البلاطات واحد
        """
        return self.board == other.board

    def __hash__(self):
        """
        بنحوّل الـ board لـ tuple علشان نقدر نخزن الـ State في set أو dict
        ده مهم جدًا علشان:
        - نتجنب تكرار الحالات
        - نحسن الأداء في البحث
        """
        return hash(tuple(self.board))
