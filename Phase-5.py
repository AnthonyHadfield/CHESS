from tkinter import *
import numpy as np
import time

class ChessWorld:
    def __init__(self):

        self.root = Tk()
        """WINDOW center"""
        self.root.geometry("780x780+535+30")
        self.root.title('CHESS BOARD'.center(200))
        self.frame = Canvas(bg='dark goldenrod', width=760, height=745)
        self.frame.pack()
        """declarations"""
        self.bc = (); self.bp = (); self.mp = ()
        self.move_white_agent = []
        self.move_black_agent = []

        # self.root.mainloop()

    def pieces(self):
        self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Rw1', 'Ktb1', 'Bw1', 'Qw'
                                   'Kw', 'Bw2', 'Ktw2', 'Rw2']
        #self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Ktw1', 'Ktw2']
        self.start_white_pieces = ['Ktw1', 'Ktw2']
        self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8', 'Rb1', 'Ktb1', 'Bb1', 'Qb' 
                                   'Kb', 'Bb2', 'Ktb2', 'Rb2']
        # self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8', 'Ktb1', 'Ktb2']
        self.start_black_pieces = ['Ktb1', 'Ktb2']

    def board_data(self):

        x = 8; y = 8
        """bc = board_coordinates"""
        self.bc = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.bc[0][0] = (34, 30); self.bc[0][1] = (124, 30); self.bc[0][2] = (214, 30); self.bc[0][3] = (304, 30)
        self.bc[0][4] = (394, 30); self.bc[0][5] = (484, 30); self.bc[0][6] = (574, 30); self.bc[0][7] = (664, 30)
        """row 7 coordinates"""
        self.bc[1][0] = (34, 118); self.bc[1][1] = (124, 118); self.bc[1][2] = (214, 118); self.bc[1][3] = (304, 118)
        self.bc[1][4] = (394, 118); self.bc[1][5] = (484, 118); self.bc[1][6] = (574, 118); self.bc[1][7] = (664, 118)
        """row 6 coordinates"""
        self.bc[2][0] = (34, 206); self.bc[2][1] = (124, 206); self.bc[2][2] = (214, 206); self.bc[2][3] = (304, 206)
        self.bc[2][4] = (394, 206); self.bc[2][5] = (484, 206); self.bc[2][6] = (574, 206); self.bc[2][7] = (664, 206)
        """row 5 coordinates"""
        self.bc[3][0] = (34, 294); self.bc[3][1] = (124, 294); self.bc[3][2] = (214, 294); self.bc[3][3] = (304, 294)
        self.bc[3][4] = (394, 294); self.bc[3][5] = (484, 294); self.bc[3][6] = (574, 294); self.bc[3][7] = (664, 294)
        """row 4 coordinates"""
        self.bc[4][0] = (34, 382); self.bc[4][1] = (124, 382); self.bc[4][2] = (214, 382); self.bc[4][3] = (304, 382)
        self.bc[4][4] = (394, 382); self.bc[4][5] = (484, 382); self.bc[4][6] = (574, 382); self.bc[4][7] = (664, 382)
        """row 3 coordinates"""
        self.bc[5][0] = (34, 470); self.bc[5][1] = (124, 470); self.bc[5][2] = (214, 470); self.bc[5][3] = (304, 470)
        self.bc[5][4] = (394, 470); self.bc[5][5] = (484, 470); self.bc[5][6] = (574, 470); self.bc[5][7] = (664, 470)
        """row 2 coordinates"""
        self.bc[6][0] = (34, 558); self.bc[6][1] = (124, 558); self.bc[6][2] = (214, 558); self.bc[6][3] = (304, 558)
        self.bc[6][4] = (394, 558); self.bc[6][5] = (484, 558); self.bc[6][6] = (574, 558); self.bc[6][7] = (664, 558)
        """row 1 coordinates"""
        self.bc[7][0] = (34, 646); self.bc[7][1] = (124, 646); self.bc[7][2] = (214, 646); self.bc[7][3] = (304, 646)
        self.bc[7][4] = (394, 646); self.bc[7][5] = (484, 646); self.bc[7][6] = (574, 646); self.bc[7][7] = (664, 646)
        """mp = move_pieces"""
        self.mp = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.mp[0][0] = 'Rb1'; self.mp[0][1] = 'Ktb1'; self.mp[0][2] = 'Bb1'; self.mp[0][3] = 'Qb'
        self.mp[0][4] = 'Kb'; self.mp[0][5] = 'Bb2'; self.mp[0][6] = 'Ktb2'; self.mp[0][7] = 'Rb2'
        """row 7 coordinates"""
        self.mp[1][0] = 'Pb1'; self.mp[1][1] = 'Pb2'; self.mp[1][2] = 'Pb3'; self.mp[1][3] = 'Pb4'
        self.mp[1][4] = 'Pb5'; self.mp[1][5] = 'Pb6'; self.mp[1][6] = 'Pb7'; self.mp[1][7] = 'Pb8'
        """row 6 coordinates"""
        self.mp[2][0] = '   '; self.mp[2][1] = '   '; self.mp[2][2] = '   '; self.mp[2][3] = '   '
        self.mp[2][4] = '   '; self.mp[2][5] = '   '; self.mp[2][6] = '   '; self.mp[2][7] = '   '
        """row 5 coordinates"""
        self.mp[3][0] = '   '; self.mp[3][1] = '   '; self.mp[3][2] = '   '; self.mp[3][3] = '   '
        self.mp[3][4] = '   '; self.mp[3][5] = '   '; self.mp[3][6] = '   '; self.mp[3][7] = '   '
        """row 4 coordinates"""
        self.mp[4][0] = '   '; self.mp[4][1] = '   '; self.mp[4][2] = '   '; self.mp[4][3] = '   '
        self.mp[4][4] = '   '; self.mp[4][5] = '   '; self.mp[4][6] = '   '; self.mp[4][7] = '   '
        """row 3 coordinates"""
        self.mp[5][0] = '   '; self.mp[5][1] = '   '; self.mp[5][2] = '   '; self.mp[5][3] = '   '
        self.mp[5][4] = '   '; self.mp[5][5] = '   '; self.mp[5][6] = '   '; self.mp[5][7] = '   '
        """row 2 coordinates"""
        self.mp[6][0] = 'Pw1'; self.mp[6][1] = 'Pw2'; self.mp[6][2] = 'Pw3'; self.mp[6][3] = 'Pw4'
        self.mp[6][4] = 'Pw5'; self.mp[6][5] = 'Pw6'; self.mp[6][6] = 'Pw7'; self.mp[6][7] = 'Pw8'
        """row 1 coordinates"""
        self.mp[7][0] = 'Rw1'; self.mp[7][1] = 'Ktw1'; self.mp[7][2] = 'Bw1'; self.mp[7][3] = 'Qw'
        self.mp[7][4] = 'Kw'; self.mp[7][5] = 'Bw2'; self.mp[7][6] = 'Ktw2'; self.mp[7][7] = 'Rw2'
        np.save('C:/Users/user/PycharmProjects/CHESS/Move_piece', self.mp)

    def board(self):
        self.board_data()
        """frame off sets """
        x1 = 90; x2 = 180; x3 = 270; x4 = 360; x5 = 450; x6 = 540; x7 = 630; y1 = 88
        self.frame.create_rectangle(22, 22, 670, 670, fill='lime green')
        """row 8"""
        self.frame.create_rectangle(20, 17, 110, 105, fill='light yellow')
        self.frame.create_rectangle(20 + x1, 17, 110 + x1, 105, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x2, 17, 110 + x2, 105, fill='light yellow')
        self.frame.create_rectangle(20 + x3, 17, 110 + x3, 105, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x4, 17, 110 + x4, 105, fill='light yellow')
        self.frame.create_rectangle(20 + x5, 17, 110 + x5, 105, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x6, 17, 110 + x6, 105, fill='light yellow')
        self.frame.create_rectangle(20 + x7, 17, 110 + x7, 105, fill='darkolivegreen4')
        """row 7"""
        self.frame.create_rectangle(20, 17 + y1, 110, 105 + y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x1, 17 + y1, 110 + x1, 105 + y1, fill='light yellow')
        self.frame.create_rectangle(20 + x2, 17 + y1, 110 + x2, 105 + y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x3, 17 + y1, 110 + x3, 105 + y1, fill='light yellow')
        self.frame.create_rectangle(20 + x4, 17 + y1, 110 + x4, 105 + y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x5, 17 + y1, 110 + x5, 105 + y1, fill='light yellow')
        self.frame.create_rectangle(20 + x6, 17 + y1, 110 + x6, 105 + y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x7, 17 + y1, 110 + x7, 105 + y1, fill='light yellow')
        """row 6"""
        self.frame.create_rectangle(20, 17 + 2 * y1, 110, 105 + 2 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x1, 17 + 2 * y1, 110 + x1, 105 + 2 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x2, 17 + 2 * y1, 110 + x2, 105 + 2 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x3, 17 + 2 * y1, 110 + x3, 105 + 2 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x4, 17 + 2 * y1, 110 + x4, 105 + 2 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x5, 17 + 2 * y1, 110 + x5, 105 + 2 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x6, 17 + 2 * y1, 110 + x6, 105 + 2 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x7, 17 + 2 * y1, 110 + x7, 105 + 2 * y1, fill='darkolivegreen4')
        """row 5"""
        self.frame.create_rectangle(20, 17 + 3 * y1, 110, 105 + 3 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x1, 17 + 3 * y1, 110 + x1, 105 + 3 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x2, 17 + 3 * y1, 110 + x2, 105 + 3 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x3, 17 + 3 * y1, 110 + x3, 105 + 3 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x4, 17 + 3 * y1, 110 + x4, 105 + 3 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x5, 17 + 3 * y1, 110 + x5, 105 + 3 * y1, fill='light yellow')
        self.frame.create_rectangle(20 + x6, 17 + 3 * y1, 110 + x6, 105 + 3 * y1, fill='darkolivegreen4')
        self.frame.create_rectangle(20 + x7, 17 + 3 * y1, 110 + x7, 105 + 3 * y1, fill='light yellow')
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
        """BOARDER"""
        self.frame.create_line(22, 18, 740, 18, 740, 720, 22, 720, 22, 18, fill='black', width=5)
        """TEXT"""
        d = 88; e = 90
        self.frame.create_text(11, 64, text='8', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + d, text='7', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + 2 * d, text='6', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + 3 * d, text='5', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + 4 * d, text='4', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + 5 * d, text='3', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + 6 * d, text='2', font="Verdana 12 bold", fill='white')
        self.frame.create_text(11, 64 + 7 * d, text='1', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66, 64 + 7.61 * d, text='A', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + e, 64 + 7.61 * d, text='B', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + 2 * e, 64 + 7.61 * d, text='C', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + 3 * e, 64 + 7.61 * d, text='D', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + 4 * e, 64 + 7.61 * d, text='E', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + 5 * e, 64 + 7.61 * d, text='F', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + 6 * e, 64 + 7.61 * d, text='G', font="Verdana 12 bold", fill='white')
        self.frame.create_text(66 + 7 * e, 64 + 7.61 * d, text='H', font="Verdana 12 bold", fill='white')
        """black pieces"""
        self.img_rook1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook1_b.png')
        self.Rb1 = self.frame.create_image(self.bc[0][0], anchor=NW, image=self.img_rook1_b)
        self.img_knight1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_b.png')
        self.Ktb1 = self.frame.create_image(self.bc[0][1], anchor=NW, image=self.img_knight1_b)
        self.img_bishop1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_b.png')
        self.Bb1 = self.frame.create_image(self.bc[0][2], anchor=NW, image=self.img_bishop1_b)
        self.img_queen_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b.png')
        self.Qb = self.frame.create_image(self.bc[0][3], anchor=NW, image=self.img_queen_b)
        self.img_king_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_b.png')
        self.Kb = self.frame.create_image(self.bc[0][4], anchor=NW, image=self.img_king_b)
        self.img_bishop2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_b.png')
        self.Bb2 = self.frame.create_image(self.bc[0][5], anchor=NW, image=self.img_bishop2_b)
        self.img_knight2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_b.png')
        self.Ktb2 = self.frame.create_image(self.bc[0][6], anchor=NW, image=self.img_knight2_b)
        self.img_rook2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_b.png')
        self.Rb2 = self.frame.create_image(self.bc[0][7], anchor=NW, image=self.img_rook2_b)
        self.img_pawn1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn1_b.png')
        self.Pb1 = self.frame.create_image(self.bc[1][0], anchor=NW, image=self.img_pawn1_b)
        self.img_pawn2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn2_b.png')
        self.Pb2 = self.frame.create_image(self.bc[1][1], anchor=NW, image=self.img_pawn2_b)
        self.img_pawn3_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn3_b.png')
        self.Pb3 = self.frame.create_image(self.bc[1][2], anchor=NW, image=self.img_pawn3_b)
        self.img_pawn4_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn4_b.png')
        self.Pb4 = self.frame.create_image(self.bc[1][3], anchor=NW, image=self.img_pawn4_b)
        self.img_pawn5_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn5_b.png')
        self.Pb5 = self.frame.create_image(self.bc[1][4], anchor=NW, image=self.img_pawn5_b)
        self.img_pawn6_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn6_b.png')
        self.Pb6 = self.frame.create_image(self.bc[1][5], anchor=NW, image=self.img_pawn6_b)
        self.img_pawn7_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn7_b.png')
        self.Pb7 = self.frame.create_image(self.bc[1][6], anchor=NW, image=self.img_pawn7_b)
        self.img_pawn8_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn8_b.png')
        self.Pb8 = self.frame.create_image(self.bc[1][7], anchor=NW, image=self.img_pawn8_b)
        """white pieces"""
        self.img_rook1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook1_w.png')
        self.Rw1 = self.frame.create_image(self.bc[7][0], anchor=NW, image=self.img_rook1_w)
        self.img_knight1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_w.png')
        self.Ktw1 = self.frame.create_image(self.bc[7][1], anchor=NW, image=self.img_knight1_w)
        self.img_bishop1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_w.png')
        self.Bw1 = self.frame.create_image(self.bc[7][2], anchor=NW, image=self.img_bishop1_w)
        self.img_queen_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w.png')
        self.Qw = self.frame.create_image(self.bc[7][3], anchor=NW, image=self.img_queen_w)
        self.img_king_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_w.png')
        self.Kw = self.frame.create_image(self.bc[7][4], anchor=NW, image=self.img_king_w)
        self.img_bishop2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_w.png')
        self.Bw2 = self.frame.create_image(self.bc[7][5], anchor=NW, image=self.img_bishop2_w)
        self.img_knight2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_w.png')
        self.Ktw2 = self.frame.create_image(self.bc[7][6], anchor=NW, image=self.img_knight2_w)
        self.img_rook2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_w.png')
        self.Rw2 = self.frame.create_image(self.bc[7][7], anchor=NW, image=self.img_rook2_w)
        self.img_pawn1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn1_w.png')
        self.Pw1 = self.frame.create_image(self.bc[6][0], anchor=NW, image=self.img_pawn1_w)
        self.img_pawn2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn2_w.png')
        self.Pw2 = self.frame.create_image(self.bc[6][1], anchor=NW, image=self.img_pawn2_w)
        self.img_pawn3_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn3_w.png')
        self.Pw3 = self.frame.create_image(self.bc[6][2], anchor=NW, image=self.img_pawn3_w)
        self.img_pawn4_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn4_w.png')
        self.Pw4 = self.frame.create_image(self.bc[6][3], anchor=NW, image=self.img_pawn4_w)
        self.img_pawn5_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn5_w.png')
        self.Pw5 = self.frame.create_image(self.bc[6][4], anchor=NW, image=self.img_pawn5_w)
        self.img_pawn6_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn6_w.png')
        self.Pw6 = self.frame.create_image(self.bc[6][5], anchor=NW, image=self.img_pawn6_w)
        self.img_pawn7_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn7_w.png')
        self.Pw7 = self.frame.create_image(self.bc[6][6], anchor=NW, image=self.img_pawn7_w)
        self.img_pawn8_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn8_w.png')
        self.Pw8 = self.frame.create_image(self.bc[6][7], anchor=NW, image=self.img_pawn8_w)

        #self.root.mainloop()

    def white_pawn(self):
        if self.i_white_index == 6:
            self.potential_coords_vector = [(self.bc[5][self.white_choice]), (self.bc[4][self.white_choice])]
            self.potential_board_vector = [(self.mp[5][self.white_choice]), (self.mp[4][self.white_choice])]
            """If 1st move is blocked select 2nd"""
            if self.potential_board_vector[0] != '   ' and self.potential_board_vector[1] == '   ':
                self.white_move_vector.append(self.potential_coords_vector[1])
                """If 2nd move is blocked select 1st only"""
            elif self.potential_board_vector[0] == '   ' and self.potential_board_vector[1] != '   ':
                self.white_move_vector.append(self.potential_coords_vector[0])
                """If BOTH 1st/2nd moves available select randomly """
            elif self.potential_board_vector[0] == '   ' and self.potential_board_vector[1] == '   ':
                self.white_move_vector.append(self.potential_coords_vector[0])
                self.white_move_vector.append(self.potential_coords_vector[1])
                # print('WHITE', self.white_move_vector)
                #break

    def white_knight(self, i, j):
        self.white_move_vector = []
        self.white_board_vector = []
        index = [[1, -2], [-1, -2], [-2, 1], [-2, -1], [1, 2], [-1, 2], [2, 1], [2, -1]]
        print('selected piece index', i, j)
        """define adjusted index"""
        for x in range(0, 8):
            index[x][0] = index[x][0] + i
            index[x][1] = index[x][1] + j
        """define index off board positions to be removed"""
        remove1 = []
        """REMOVE DOWN"""
        for i in range(0, len(index)):
            if index[i][0] > 7:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index.pop(remove1[i] - i)
        remove2 = []
        """REMOVE LEFT"""
        for i in range(0, len(index)):
            if index[i][1] < 0:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index.pop(remove2[i] - i)
        remove3 = []
        """REMOVE RIGHT"""
        for i in range(0, len(index)):
            if index[i][1] > 7:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index.pop(remove3[i] - i)
        remove4 = []
        """REMOVE UP"""
        for i in range(0, len(index)):
            if index[i][0] < 0:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index.pop(remove4[i] - i)
        print('final WHITE INDEX result', index)
        '''convert index to coords and pieces'''
        for x in range(0, len(index)):
            coords = self.bc[index[x][0]][index[x][1]]
            vector = self.mp[index[x][0]][index[x][1]]
            self.potential_coords_vector.append(coords)
            self.potential_white_board_vector.append(vector)
        """define final WHITE move and board vectors"""
        for x in range(0, len(index)):
            if self.potential_white_board_vector[x] != '   ':
                piece = list(self.potential_white_board_vector[x])
                for i in range(0, len(piece)):
                    if piece[i] == 'b':
                        self.white_move_vector.append(self.potential_coords_vector[x])
                        self.white_board_vector.append(self.potential_white_board_vector[x])
            elif self.potential_white_board_vector[x] == '   ':
                self.white_move_vector.append(self.potential_coords_vector[x])
                self.white_board_vector.append(self.potential_white_board_vector[x])
        print('white coords vector', self.white_move_vector)
        print('white board vector', self.white_board_vector)

    def black_knight(self, i, j):
        self.black_board_vector = []
        self.black_move_vector = []
        index = [[1, -2], [-1, -2], [-2, 1], [-2, -1], [1, 2], [-1, 2], [2, 1], [2, -1]]
        print('selected piece index', i, j)
        """define adjusted index"""
        for x in range(0, 8):
            index[x][0] = index[x][0] + i
            index[x][1] = index[x][1] + j
        print('new index', index)
        """define index off board positions to be removed"""
        remove1 = []
        """REMOVE DOWN"""
        for i in range(0, len(index)):
            if index[i][0] > 7:
                remove1.append(i)
        print(remove1)
        for i in range(0, len(remove1)):
            index.pop(remove1[i] - i)
        remove2 = []
        """REMOVE LEFT"""
        for i in range(0, len(index)):
            if index[i][1] < 0:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index.pop(remove2[i] - i)
        remove3 = []
        """REMOVE RIGHT"""
        for i in range(0, len(index)):
            if index[i][1] > 7:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index.pop(remove3[i] - i)
        remove4 = []
        """REMOVE UP"""
        for i in range(0, len(index)):
            if index[i][0] < 0:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index.pop(remove4[i] - i)
        '''convert index to coords and piece'''
        for x in range(0, len(index)):
            coords = self.bc[index[x][0]][index[x][1]]
            vector = self.mp[index[x][0]][index[x][1]]
            self.potential_coords_vector.append(coords)
            self.potential_black_board_vector.append(vector)
        """define final BLACK move and board vectors"""
        for x in range(0, len(index)):
            if self.potential_black_board_vector[x] != '   ':
                piece = list(self.potential_black_board_vector[x])
                for i in range(0, len(piece)):
                    if piece[i] == 'w':
                        self.black_move_vector.append(self.potential_coords_vector[x])
                        self.black_board_vector.append(self.potential_black_board_vector[x])
            elif self.potential_black_board_vector[x] == '   ':
                self.black_move_vector.append(self.potential_coords_vector[x])
                self.black_board_vector.append(self.potential_black_board_vector[x])
        print('white coords vector', self.black_move_vector)
        print('white board vector', self.black_board_vector)

    def white_piece_vector(self):
        """ENTER WHILE TRUE HERE"""
        while True:
            self.white_move_vector = []
            self.potential_coords_vector = []
            self.potential_white_board_vector = []
            self.white_choice = np.random.randint(0, len(self.start_white_pieces))
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.mp[i][j] == self.start_white_pieces[self.white_choice]:
                        self.selected_white_piece_coords = self.bc[i][j]
                        self.i_white_index = i
                        self.j_white_index = j
                        piece = list(self.start_white_pieces[self.white_choice])
                        print('WHITE PIECE', piece)
                        #if piece[0] == 'P':
                         #   self.white_pawn()
                        if piece[0] == 'K' and piece[1] == 't':
                            self.white_knight(i, j)
            print('')
            break

    def black_piece_vector(self):
        """ENTER WHILE TRUE HERE"""
        while True:
            self.black_move_vector = []
            self.potential_coords_vector = []
            self.potential_black_board_vector = []
            self.black_choice = np.random.randint(0, len(self.start_black_pieces))
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.mp[i][j] == self.start_black_pieces[self.black_choice]:
                        self.selected_black_piece_coords = self.bc[i][j]
                        self.i_black_index = i
                        self.j_black_index = j
                        piece = list(self.start_black_pieces[self.black_choice])
                        #if piece[0] == 'P':
                         #   self.black_pawn()
                        if piece[0] == 'K' and piece[1] == 't':
                            self.black_knight(i, j)
            print('')
            break

    def white_board_label(self):
        if self.start_white_pieces[self.white_choice] == 'Pw1':
            Pw1 = self.Pw1
            self.agent = Pw1
            print('MOVE Pw1')
        elif self.start_white_pieces[self.white_choice] == 'Pw2':
            Pw2 = self.Pw2
            self.agent = Pw2
            print('MOVE Pw2')
        elif self.start_white_pieces[self.white_choice] == 'Pw3':
            Pw3 = self.Pw3
            self.agent = Pw3
            print('MOVE Pw3')
        elif self.start_white_pieces[self.white_choice] == 'Pw4':
            Pw4 = self.Pw4
            self.agent = Pw4
            print('MOVE Pw4')
        elif self.start_white_pieces[self.white_choice] == 'Pw5':
            Pw5 = self.Pw5
            self.agent = Pw5
            print('MOVE Pw5')
        elif self.start_white_pieces[self.white_choice] == 'Pw6':
            Pw6 = self.Pw6
            self.agent = Pw6
            print('MOVE Pw6')
        elif self.start_white_pieces[self.white_choice] == 'Pw7':
            Pw7 = self.Pw7
            self.agent = Pw7
            print('MOVE Pw7')
        elif self.start_white_pieces[self.white_choice] == 'Pw8':
            Pw8 = self.Pw8
            self.agent = Pw8
            print('MOVE Pw8')
        elif self.start_white_pieces[self.white_choice] == 'Rw1':
            Rw1 = self.Rw1
            self.agent = Rw1
            print('MOVE Rw1')
        elif self.start_white_pieces[self.white_choice] == 'Bw1':
            Bw1 = self.Bw1
            self.agent = Bw1
            print('MOVE Bw1')
        elif self.start_white_pieces[self.white_choice] == 'Ktw1':
            Ktw1 = self.Ktw1
            self.agent = Ktw1
            print('MOVE Ktw1')
        elif self.start_white_pieces[self.white_choice] == 'Qw':
            Qw = self.Qw
            self.agent = Qw
            print('MOVE Qw')
        elif self.start_white_pieces[self.white_choice] == 'Kw':
            Kw = self.Kw
            self.agent = Kw
            print('MOVE Kw')
        elif self.start_white_pieces[self.white_choice] == 'Bw2':
            Bw2 = self.Bw2
            self.agent = Bw2
            print('MOVE Bw2')
        elif self.start_white_pieces[self.white_choice] == 'Ktw2':
            Ktw2 = self.Ktw2
            self.agent = Ktw2
            print('MOVE Ktw2')
        elif self.start_white_pieces[self.white_choice] == 'Rw2':
            Rw2 = self.Rw2
            self.agent = Rw2
            print('MOVE Rw2')

    def black_board_label(self):
        if self.start_black_pieces[self.black_choice] == 'Pb1':
            Pb1 = self.Pb1
            self.agent = Pb1
            print('MOVE Pb1')
        elif self.start_black_pieces[self.black_choice] == 'Pb2':
            Pb2 = self.Pb2
            self.agent = Pb2
            print('MOVE Pb2')
        elif self.start_black_pieces[self.black_choice] == 'Pb3':
            Pb3 = self.Pb3
            self.agent = Pb3
            print('MOVE Pb3')
        elif self.start_black_pieces[self.black_choice] == 'Pb4':
            Pb4 = self.Pb4
            self.agent = Pb4
            print('MOVE Pb4')
        elif self.start_black_pieces[self.black_choice] == 'Pb5':
            Pb5 = self.Pb5
            self.agent = Pb5
            print('MOVE Pb5')
        elif self.start_black_pieces[self.black_choice] == 'Pb6':
            Pb6 = self.Pb6
            self.agent = Pb6
            print('MOVE Pb6')
        elif self.start_black_pieces[self.black_choice] == 'Pb7':
            Pb7 = self.Pb7
            self.agent = Pb7
            print('MOVE Pb7')
        elif self.start_black_pieces[self.black_choice] == 'Pb8':
            Pb8 = self.Pb8
            self.agent = Pb8
            print('MOVE Pb8')
        elif self.start_black_pieces[self.black_choice] == 'Rb1':
            Rb1 = self.Rb1
            self.agent = Rb1
            print('MOVE Rb1')
        elif self.start_black_pieces[self.black_choice] == 'Ktb1':
            Ktb1 = self.Ktb1
            self.agent = Ktb1
            print('MOVE Ktb1')
        elif self.start_black_pieces[self.black_choice] == 'Bb1':
            Bb1 = self.Bb1
            self.agent = Bb1
            print('MOVE Bb1')
        elif self.start_black_pieces[self.black_choice] == 'Qb':
            Qb = self.Qb
            self.agent = Qb
            print('MOVE Qb')
        elif self.start_black_pieces[self.black_choice] == 'Kb':
            Kb = self.Kb
            self.agent = Kb
            print('MOVE Kb')
        elif self.start_black_pieces[self.black_choice] == 'Bb2':
            Bb2 = self.Bb2
            self.agent = Bb2
            print('MOVE Bb2')
        elif self.start_black_pieces[self.black_choice] == 'Ktb2':
            Ktb2 = self.Ktb2
            self.agent = Ktb2
            print('MOVE Ktb2')
        elif self.start_black_pieces[self.black_choice] == 'Rb2':
            Rb2 = self.Rb2
            self.agent = Rb2
            print('MOVE Rb2')

    def black_graphic_board_label(self):
        if self.white_board_vector[self.move] == 'Pb1':
            Pb1 = self.Pb1
            self.agent = Pb1
        elif self.white_board_vector[self.move] == 'Pb2':
            Pb2 = self.Pb2
            self.agent = Pb2
        elif self.white_board_vector[self.move] == 'Pb3':
            Pb3 = self.Pb3
            self.agent = Pb3
        elif self.white_board_vector[self.move] == 'Pb4':
            Pb4 = self.Pb4
            self.agent = Pb4
        elif self.white_board_vector[self.move] == 'Pb5':
            Pb5 = self.Pb5
            self.agent = Pb5
        elif self.white_board_vector[self.move] == 'Pb6':
            Pb6 = self.Pb6
            self.agent = Pb6
        elif self.white_board_vector[self.move] == 'Pb7':
            Pb7 = self.Pb7
            self.agent = Pb7
        elif self.white_board_vector[self.move] == 'Pb8':
            Pb8 = self.Pb8
            self.agent = Pb8
        elif self.white_board_vector[self.move] == 'Rb1':
            Rb1 = self.Rb1
            self.agent = Rb1
        elif self.white_board_vector[self.move] == 'Ktb1':
            Ktb1 = self.Ktb1
            self.agent = Ktb1
        elif self.white_board_vector[self.move] == 'Bb1':
            Bb1 = self.Bb1
            self.agent = Bb1
        elif self.white_board_vector[self.move] == 'Qb':
            Qb = self.Qb
            self.agent = Qb
        elif self.white_board_vector[self.move] == 'Kb':
            Kb = self.Kb
            self.agent = Kb
        elif self.white_board_vector[self.move] == 'Bb2':
            Bb2 = self.Bb2
            self.agent = Bb2
        elif self.white_board_vector[self.move] == 'Ktb2':
            Ktb2 = self.Ktb2
            self.agent = Ktb2
        elif self.white_board_vector[self.move] == 'Rb2':
            Rb2 = self.Rb2
            self.agent = Rb2

    def white_graphic_board_label(self):
        if self.black_board_vector[self.move] == 'Pw1':
            Pw1 = self.Pw1
            self.agent = Pw1
        elif self.black_board_vector[self.move] == 'Pw2':
            Pw2 = self.Pw2
            self.agent = Pw2
        elif self.black_board_vector[self.move] == 'Pw3':
            Pw3 = self.Pw3
            self.agent = Pw3
        elif self.black_board_vector[self.move] == 'Pw4':
            Pw4 = self.Pw4
            self.agent = Pw4
        elif self.black_board_vector[self.move] == 'Pw5':
            Pw5 = self.Pw5
            self.agent = Pw5
        elif self.black_board_vector[self.move] == 'Pw6':
            Pw6 = self.Pw6
            self.agent = Pw6
        elif self.black_board_vector[self.move] == 'Pw7':
            Pw7 = self.Pw7
            self.agent = Pw7
        elif self.black_board_vector[self.move] == 'Pw8':
            Pw8 = self.Pw8
            self.agent = Pw8
        elif self.black_board_vector[self.move] == 'Rw1':
            Rw1 = self.Rw1
            self.agent = Rw1
        elif self.black_board_vector[self.move] == 'Ktw1':
            Ktw1 = self.Ktw1
            self.agent = Ktw1
        elif self.black_board_vector[self.move] == 'Bw1':
            Bw1 = self.Bw1
            self.agent = Bw1
        elif self.black_board_vector[self.move] == 'Qw':
            Qw = self.Qw
            self.agent = Qw
        elif self.black_board_vector[self.move] == 'Kw':
            Kw = self.Kw
            self.agent = Kw
        elif self.black_board_vector[self.move] == 'Bw2':
            Bw2 = self.Bw2
            self.agent = Bw2
        elif self.black_board_vector[self.move] == 'Ktw2':
            Ktw2 = self.Ktw2
            self.agent = Ktw2
        elif self.black_board_vector[self.move] == 'Rw2':
            Rw2 = self.Rw2
            self.agent = Rw2

    def capture_black_piece(self):
        for i in range(0, len(self.start_black_pieces)):
            if self.start_black_pieces[i] == self.white_board_vector[self.move]:
                self.start_black_pieces.pop(i)
                print('NEW  BLACK  LIST', self.start_black_pieces)
                """REMOVE PIECE FROM BOARD"""
                break
        self.black_graphic_board_label()
        self.move_white_agent = []
        '''Arbitrarily move captured piece off the graphic board'''
        zero = -1000
        one = -1000
        self.move_white_agent.append(zero)
        self.move_white_agent.append(one)
        self.frame.move(self.agent, self.move_white_agent[0], self.move_white_agent[1])
        self.move_white_agent = []

    def capture_white_piece(self):
        for i in range(0, len(self.start_white_pieces)):
            if self.start_white_pieces[i] == self.black_board_vector[self.move]:
                self.start_white_pieces.pop(i)
                print('NEW  WHITE  LIST', self.start_white_pieces)
                """REMOVE PIECE FROM BOARD"""
                break
        self.white_graphic_board_label()
        self.move_black_agent = []
        zero = -1000
        one = -1000
        self.move_black_agent.append(zero)
        self.move_black_agent.append(one)
        self.frame.move(self.agent, self.move_black_agent[0], self.move_black_agent[1])
        self.frame.update()
        self.move_black_agent = []

    def move_random_piece(self):
        self.pieces()
        self.board_data()
        self.board()
        for i in range(1, 20):
            self.white_piece_vector()
            self.white_board_label()
            self.potential_white_board_vector = []
            self.potential_black_board_vector = []
            print('')
            """select random move"""
            self.move = []
            self.move = np.random.randint(0, len(self.white_board_vector))
            """MOVE piece"""
            random_piece_board_coords = self.white_move_vector[self.move]
            selection = random_piece_board_coords
            """define np move array"""
            zero = selection[0] - self.selected_white_piece_coords[0]
            one = selection[1] - self.selected_white_piece_coords[1]
            self.move_white_agent.append(zero)
            self.move_white_agent.append(one)
            """MOVE WHITE PIECE ON CHESS BOARD"""
            self.frame.move(self.agent, self.move_white_agent[0], self.move_white_agent[1])
            time.sleep(0.25)
            self.frame.update()
            self.move_white_agent = []
            """REMOVE BLACK PIECE"""
            piece = list(self.white_board_vector[self.move])
            print('PIECE', piece)
            for i in range(0, len(piece)):
                if piece[i] == 'b':
                    print('CAPTURE BLACK PIECE')
                    self.capture_black_piece()
            """update piece matrix"""
            for m in range(0, 8):
                for n in range(0, 8):
                    if self.bc[m][n] == random_piece_board_coords:
                        self.mp[m][n] == self.bc[m][n]
                        hold = self.mp[m][n]
                        self.mp[m][n] = self.mp[self.i_white_index][self.j_white_index]
                        self.mp[self.i_white_index][self.j_white_index] = hold
                        if self.mp[self.i_white_index][self.j_white_index] != '   ':
                            self.mp[self.i_white_index][self.j_white_index] = '   '
                        np.save('C:/Users/user/PycharmProjects/CHESS/Move_piece', self.mp)
                        print(self.mp)
            """MOVE BLACK PIECES"""
            self.black_piece_vector()
            self.black_board_label()
            self.move = []
            self.move = np.random.randint(0, len(self.black_board_vector))
            """MOVE piece"""
            random_piece_board_coords = self.black_move_vector[self.move]
            selection = random_piece_board_coords
            """define np move array"""
            zero = selection[0] - self.selected_black_piece_coords[0]
            one = selection[1] - self.selected_black_piece_coords[1]
            self.move_black_agent.append(zero)
            self.move_black_agent.append(one)
            """MOVE BLACK PIECE ON CHESS BOARD"""
            self.frame.move(self.agent, self.move_black_agent[0], self.move_black_agent[1])
            self.move_black_agent = []
            time.sleep(0.25)
            self.frame.update()
            """REMOVE BLACK PIECE"""
            piece = list(self.black_board_vector[self.move])
            for i in range(0, len(piece)):
                if piece[i] == 'w':
                    print('CAPTURE WHITE PIECE')
                    self.capture_white_piece()
            """update piece matrix"""
            for m in range(0, 8):
                for n in range(0, 8):
                    if self.bc[m][n] == random_piece_board_coords:
                        self.mp[m][n] == self.bc[m][n]
                        hold = self.mp[m][n]
                        self.mp[m][n] = self.mp[self.i_black_index][self.j_black_index]
                        self.mp[self.i_black_index][self.j_black_index] = hold
                        if self.mp[self.i_black_index][self.j_black_index] != '   ':
                            self.mp[self.i_black_index][self.j_black_index] = '   '
                        np.save('C:/Users/user/PycharmProjects/CHESS/Move_piece', self.mp)
                        print(self.mp)

        self.root.mainloop()


data = ChessWorld()

data.board()
# data.board_data()
#data.white_piece_vector()
# data.black_piece_vector()
#data.random_white_move()
data.move_random_piece()
# data.white_board_label()
# data.black_board_label()

