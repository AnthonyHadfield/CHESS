import tkinter as tk
import numpy as np
import time

class chessworld:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='dark goldenrod', height=760, width=760)
        self.frame.pack()

    def board(self):
        """frame"""
        """off sets"""
        x1 = 90; x2 = 180; x3 = 270; x4 = 360; x5 = 450; x6 = 540; x7 = 630; x8 = 720
        y1 = 88; y2 = 176; y3 = 264; y4 = 352; y5 = 440; y6 = 528; y7 = 616; y8= 702

        self.frame.create_rectangle(22, 22, 670, 670, fill='lime green')
        """row 8"""
        self.frame.create_rectangle(20, 17, 110, 105, fill='light yellow')
        self.frame.create_rectangle(20+x1, 17, 110+x1, 105, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x2, 17, 110+x2, 105, fill='light yellow')
        self.frame.create_rectangle(20+x3, 17, 110+x3, 105, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x4, 17, 110+x4, 105, fill='light yellow')
        self.frame.create_rectangle(20+x5, 17, 110+x5, 105, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x6, 17, 110 + x6, 105, fill='light yellow')
        self.frame.create_rectangle(20+x7, 17, 110 + x7, 105, fill='darkolivegreen4')
        """row 7"""
        self.frame.create_rectangle(20, 17+y1, 110, 105+y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x1, 17+y1, 110+x1, 105+y1, fill='light yellow')
        self.frame.create_rectangle(20+x2, 17+y1, 110+x2, 105+y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x3, 17+y1, 110+x3, 105+y1, fill='light yellow')
        self.frame.create_rectangle(20+x4, 17+y1, 110+x4, 105+y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x5, 17+y1, 110+x5, 105+y1, fill='light yellow')
        self.frame.create_rectangle(20+x6, 17+y1, 110+x6, 105+y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20+x7, 17+y1, 110+x7, 105+y1, fill='light yellow')
        """row 6"""
        self.frame.create_rectangle(20, 17 + 2*y1, 110, 105 + 2*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x1, 17 + 2*y1, 110 + x1, 105 + 2*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x2, 17 + 2*y1, 110 + x2, 105 + 2*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x3, 17 + 2*y1, 110 + x3, 105 + 2*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x4, 17 + 2*y1, 110 + x4, 105 + 2*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x5, 17 + 2*y1, 110 + x5, 105 + 2*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x6, 17 + 2*y1, 110 + x6, 105 + 2*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x7, 17 + 2*y1, 110 + x7, 105 + 2*y1, fill='darkolivegreen4')
        """row 5"""
        self.frame.create_rectangle(20, 17 + 3*y1, 110, 105 + 3*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x1, 17 + 3*y1, 110 + x1, 105 + 3*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x2, 17 + 3*y1, 110 + x2, 105 + 3*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x3, 17 + 3*y1, 110 + x3, 105 + 3*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x4, 17 + 3*y1, 110 + x4, 105 + 3*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x5, 17 + 3*y1, 110 + x5, 105 + 3*y1, fill='light yellow')
        self.frame.create_rectangle(20 + x6, 17 + 3*y1, 110 + x6, 105 + 3*y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x7, 17 + 3*y1, 110 + x7, 105 + 3*y1, fill='light yellow')
        """row 4"""
        self.frame.create_rectangle(20, 17 + 4 * y1, 110, 105 + 4 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x1, 17 + 4 * y1, 110 + x1, 105 + 4 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x2, 17 + 4 * y1, 110 + x2, 105 + 4 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x3, 17 + 4 * y1, 110 + x3, 105 + 4 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x4, 17 + 4 * y1, 110 + x4, 105 + 4 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x5, 17 + 4 * y1, 110 + x5, 105 + 4 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x6, 17 + 4 * y1, 110 + x6, 105 + 4 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x7, 17 + 4 * y1, 110 + x7, 105 + 4 * y1, fill='darkolivegreen4')
        """row 3"""
        self.frame.create_rectangle(20, 17 + 5 * y1, 110, 105 + 5 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x1, 17 + 5 * y1, 110 + x1, 105 + 5 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x2, 17 + 5 * y1, 110 + x2, 105 + 5 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x3, 17 + 5 * y1, 110 + x3, 105 + 5 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x4, 17 + 5 * y1, 110 + x4, 105 + 5 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x5, 17 + 5 * y1, 110 + x5, 105 + 5 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x6, 17 + 5 * y1, 110 + x6, 105 + 5 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x7, 17 + 5 * y1, 110 + x7, 105 + 5 * y1, fill='light yellow')
        """row 2"""
        self.frame.create_rectangle(20, 17 + 6 * y1, 110, 105 + 6 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x1, 17 + 6 * y1, 110 + x1, 105 + 6 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x2, 17 + 6 * y1, 110 + x2, 105 + 6 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x3, 17 + 6 * y1, 110 + x3, 105 + 6 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x4, 17 + 6 * y1, 110 + x4, 105 + 6 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x5, 17 + 6 * y1, 110 + x5, 105 + 6 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x6, 17 + 6 * y1, 110 + x6, 105 + 6 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x7, 17 + 6 * y1, 110 + x7, 105 + 6 * y1, fill='darkolivegreen4')
        """row 1"""
        self.frame.create_rectangle(20, 17 + 7 * y1, 110, 105 + 7 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x1, 17 + 7 * y1, 110 + x1, 105 + 7 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x2, 17 + 7 * y1, 110 + x2, 105 + 7 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x3, 17 + 7 * y1, 110 + x3, 105 + 7 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x4, 17 + 7 * y1, 110 + x4, 105 + 7 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x5, 17 + 7 * y1, 110 + x5, 105 + 7 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x6, 17 + 7 * y1, 110 + x6, 105 + 7 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x7, 17 + 7 * y1, 110 + x7, 105 + 7 * y1, fill='light yellow')

        self.root.mainloop()


data = chessworld()

data.board()