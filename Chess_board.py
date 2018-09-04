from tkinter import *

import numpy as np


class ChessWorld:

    def __init__(self):

        self.root = Tk()
        """WINDOW center"""
        self.root.geometry("780x780+535+30")
        self.root.title('CHESS BOARD'.center(200))

        self.frame = Canvas(bg='dark goldenrod', width=760, height=745)
        self.frame.pack()

        self.rook1_b = []; self.rook1_w = []; self.rook2_b = []; self.rook2_w = []; self.knight1_w = [];
        self.knight1_b = []; self.knight2_w = []; self.knight2_b = []; self.bishop1_w = []; self.bishop1_b = []
        self.bishop2_w = []; self.bishop2_b = []; self.queen_w = []; self.queen_b = []; self.king_w = []
        self.king_b = []; self.pawn1_w = []; self.pawn2_w = []; self.pawn3_w = []; self.pawn4_w = []; self.pawn5_w = []
        self.pawn6_w = []; self.pawn7_w = []; self.pawn8_w = []; self.pawn1_b = []; self.pawn2_b = []; self.pawn3_b = []
        self.pawn4_b = []; self.pawn5_b = []; self.pawn6_b = (); self.pawn7_b = (); self.pawn8_b = ()
        self.a1 = []; self.a2 = []; self.a3 = []; self.a4 = []; self.a5 = []; self.a6 = []; self.a7 = []; self.a8 = []
        self.b1 = []; self.b2 = []; self.b3 = []; self.b4 = []; self.b5 = []; self.b6 = []; self.b7 = []; self.b8 = []
        self.c1 = []; self.c2 = []; self.c3 = []; self.c4 = []; self.c5 = []; self.c6 = []; self.c7 = []; self.c8 = []
        self.d1 = []; self.d2 = []; self.d3 = []; self.d4 = []; self.d5 = []; self.d6 = []; self.d7 = []; self.d8 = []
        self.e1 = []; self.e2 = []; self.e3 = []; self.e4 = []; self.e5 = []; self.e6 = []; self.e7 = []; self.e8 = []
        self.f1 = []; self.f2 = []; self.f3 = []; self.f4 = []; self.f5 = []; self.f6 = []; self.f7 = []; self.f8 = []
        self.g1 = []; self.g2 = []; self.g3 = []; self.g4 = []; self.g5 = []; self.g6 = []; self.g7 = []; self.g8 = []
        self.h1 = []; self.h2 = []; self.h3 = []; self.h4 = []; self.h5 = []; self.h6 = []; self.h7 = []; self.h8 = []
        self.white_pieces = []; self.black_pieces = []

    def piece_positions(self):

        self.a1 = (34, 646); self.a2 = (34, 558); self.a3 = (34, 470); self.a4 = (34, 382); self.a5 = (34, 294);
        self.a6 = (34, 206); self.a7 = (34, 118); self.a8 = (34, 30); self.b1 = (124, 646); self.b2 = (124, 558);
        self.b3 = (124, 470); self.b4 = (124, 382); self.b5 = (124, 294); self.b6 = (124, 206); self.b7 = (124, 118);
        self.b8 = (124, 30); self.c1 = (214, 646); self.c2 = (214, 558); self.c3 = (214, 470); self.c4 = (214, 382);
        self.c5 = (214, 294); self.c6 = (214, 206); self.c7 = (214, 118); self.c8 = (214, 30); self.d1 = (304, 646);
        self.d2 = (304, 558); self.d3 = (304, 470); self.d4 = (304, 382); self.d5 = (304, 294); self.d6 = (304, 206);
        self.d7 = (304, 118); self.d8 = (304, 30); self.e1 = (394, 646); self.e2 = (394, 558); self.e3 = (394, 470);
        self.e4 = (394, 382); self.e5 = (394, 294); self.e6 = (394, 206); self.e7 = (394, 118); self.e8 = (394, 30);
        self.f1 = (484, 646); self.f2 = (484, 558); self.f3 = (484, 470); self.f4 = (484, 382); self.f5 = (484, 294);
        self.f6 = (484, 206); self.f7 = (484, 118); self.f8 = (484, 30); self.g1 = (574, 646); self.g2 = (574, 558);
        self.g3 = (574, 470); self.g4 = (574, 382); self.g5 = (574, 294); self.g6 = (574, 206); self.g7 = (574, 118);
        self.g8 = (574, 30); self.h1 = (664, 646); self.h2 = (664, 558); self.h3 = (664, 470); self.h4 = (664, 382);
        self.h5 = (664, 294); self.h6 = (664, 206); self.h7 = (664, 118); self.h8 = (664, 30)

        self.rook1_w = [self.a1]; self.knight1_w = [self.b1]; self.bishop1_w = [self.c1]; self.queen_w = [self.d1]
        self.king_w = [self.e1]; self.bishop2_w = [self.f1]; self.knight2_w = [self.g1]; self.rook2_w = [self.h1]
        self.pawn1_w = [self.a2]; self.pawn2_w = [self.b2]; self.pawn3_w = [self.c2]; self.pawn4_w = [self.d2]
        self.pawn5_w = [self.e2]; self.pawn6_w = [self.f2]; self.pawn7_w = [self.g2]; self.pawn8_w = [self.h2]
        self.rook1_b = [self.a8]; self.knight1_b = [self.b8]; self.bishop1_b = [self.c8]; self.queen_b = [self.d8]
        self.king_b = [self.e8]; self.bishop2_b = [self.f8]; self.knight2_b = [self.g8]; self.rook2_b = [self.h8]
        self.pawn1_b = [self.a7]; self.pawn2_b = [self.b7]; self.pawn3_b = [self.c7]; self.pawn4_b = [self.d7]
        self.pawn5_b = [self.e7]; self.pawn6_b = [self.f7]; self.pawn7_b = [self.g7]; self.pawn8_b = [self.h7]

        self.white_pieces = [['pawn1_w', self.pawn1_w], ['pawn2_w', self.pawn2_w], ['pawn3_w', self.pawn3_w],
                             ['pawn4_w',self.pawn4_w], ['pawn5_w', self.pawn5_w], ['pawn6_w', self.pawn6_w],
                             ['pawn7_w', self.pawn7_w], [ 'pawn8_w', self.pawn8_w], ['rook1_w', self.rook1_w],
                             ['knight1_w', self.knight1_w], ['bishop1_w', self.bishop1_w], ['queen_w', self.queen_w],
                             ['king_w', self.king_w], ['bishop2_w', self.bishop2_w], ['knight2_w', self.knight2_w],
                             ['rook2_w', self.rook2_w]]

        self.black_pieces = [['pawn1_b', self.pawn1_b], ['pawn2_b', self.pawn2_b], ['pawn3_b', self.pawn3_b],
                             ['pawn4_b', self.pawn4_b], ['pawn5_b', self.pawn5_b], ['pawn6_b', self.pawn6_b],
                             ['pawn7_b', self.pawn7_b], ['pawn8_b', self.pawn8_b], ['rook1_b', self.rook1_b],
                             ['knight1_b', self.knight1_b], ['bishop1_b', self.bishop1_b], ['queen_b', self.queen_b],
                             ['king_b', self.king_b], ['bishop2_b', self.bishop2_b], ['knight2_b', self.knight2_b],
                             ['rook2_b', self.rook2_b]]

    def posval(self):

        """this function imports current board position, and gets an identifier value for it, and assigns its
        value_functions for white and black side to be zero. """

        self.datachess64 = np.array([[-5], [-3], [-6], [-8], [-4], [-7], [-3], [-5],
                                     [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-2],
                                     [9], [9], [9], [9], [9], [9], [9], [9],
                                     [9], [9], [9], [9], [9], [9], [9], [9],
                                     [9], [9], [9], [9], [9], [9], [9], [9],
                                     [9], [9], [9], [9], [9], [9], [9], [9],
                                     [2], [2], [2], [2], [2], [2], [2], [2],
                                     [5], [3], [6], [8], [4], [7], [3], [5]])

        datachess64_val = np.array([])
        board_pos_value = []
        board_value_dataset = []
        current_pos_value = []

        value = 0

        for i in range(1, 65):

            value = value + (self.datachess64[i-1]* i)

        print('value = ', value)

        board_pos_value = np.append(board_pos_value, [value])
        board_pos_value = np.append(board_pos_value, [0])
        board_pos_value = np.append(board_pos_value, [-value])
        board_pos_value = np.append(board_pos_value, [0])

        print('board value', board_pos_value)


        board_value_dataset = np.append(board_value_dataset,  board_pos_value)

        print('dataset =', board_value_dataset)

        for i in range(0, len(board_value_dataset)):

            if value in board_value_dataset:

                print(board_value_dataset[i])

                current_pos_value = np.append(current_pos_value,  board_value_dataset[i])

                print('current position value =', current_pos_value)





    def board(self):

        self.piece_positions()

        """frame"""
        """off sets"""
        x1 = 90; x2 = 180; x3 = 270; x4 = 360; x5 = 450; x6 = 540; x7 = 630
        y1 = 88
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
        self.frame.create_image(self.rook1_b[0], anchor=NW, image=self.img_rook1_b)
        self.img_knight1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_b.png')
        self.frame.create_image(self.knight1_b[0], anchor=NW, image=self.img_knight1_b)
        self.img_bishop1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_b.png')
        self.frame.create_image(self.bishop1_b[0], anchor=NW, image=self.img_bishop1_b)
        self.img_queen_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b.png')
        self.frame.create_image(self.queen_b[0], anchor=NW, image=self.img_queen_b)
        self.img_king_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_b.png')
        self.frame.create_image(self.king_b[0], anchor=NW, image=self.img_king_b)
        self.img_bishop2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_b.png')
        self.frame.create_image(self.bishop2_b[0], anchor=NW, image=self.img_bishop2_b)
        self.img_knight2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_b.png')
        self.frame.create_image(self.knight2_b[0], anchor=NW, image=self.img_knight2_b)
        self.img_rook2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_b.png')
        self.frame.create_image(self.rook2_b[0], anchor=NW, image=self.img_rook2_b)
        self.img_pawn1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn1_b.png')
        self.frame.create_image(self.pawn1_b[0], anchor=NW, image=self.img_pawn1_b)
        self.img_pawn2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn2_b.png')
        self.frame.create_image(self.pawn2_b[0], anchor=NW, image=self.img_pawn2_b)
        self.img_pawn3_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn3_b.png')
        self.frame.create_image(self.pawn3_b[0], anchor=NW, image=self.img_pawn3_b)
        self.img_pawn4_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn4_b.png')
        self.frame.create_image(self.pawn4_b[0], anchor=NW, image=self.img_pawn4_b)
        self.img_pawn5_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn5_b.png')
        self.frame.create_image(self.pawn5_b[0], anchor=NW, image=self.img_pawn5_b)
        self.img_pawn6_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn6_b.png')
        self.frame.create_image(self.pawn6_b[0], anchor=NW, image=self.img_pawn6_b)
        self.img_pawn7_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn7_b.png')
        self.frame.create_image(self.pawn7_b[0], anchor=NW, image=self.img_pawn7_b)
        self.img_pawn8_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn8_b.png')
        self.frame.create_image(self.pawn8_b[0], anchor=NW, image=self.img_pawn8_b)
        """white pieces"""
        self.img_rook1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook1_w.png')
        self.frame.create_image(self.rook1_w[0], anchor=NW, image=self.img_rook1_w)
        self.img_knight1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_w.png')
        self.frame.create_image(self.knight1_w[0], anchor=NW, image=self.img_knight1_w)
        self.img_bishop1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_w.png')
        self.frame.create_image(self.bishop1_w[0], anchor=NW, image=self.img_bishop1_w)
        self.img_queen_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w.png')
        self.frame.create_image(self.queen_w[0], anchor=NW, image=self.img_queen_w)
        self.img_king_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_w.png')
        self.frame.create_image(self.king_w[0], anchor=NW, image=self.img_king_w)
        self.img_bishop2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_w.png')
        self.frame.create_image(self.bishop2_w[0], anchor=NW, image=self.img_bishop2_w)
        self.img_knight2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_w.png')
        self.frame.create_image(self.knight2_w[0], anchor=NW, image=self.img_knight2_w)
        self.img_rook2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_w.png')
        self.frame.create_image(self.rook2_w[0], anchor=NW, image=self.img_rook2_w)
        self.img_pawn1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn1_w.png')
        self.frame.create_image(self.pawn1_w[0], anchor=NW, image=self.img_pawn1_w)
        self.img_pawn2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn2_w.png')
        self.frame.create_image(self.pawn2_w[0], anchor=NW, image=self.img_pawn2_w)
        self.img_pawn3_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn3_w.png')
        self.frame.create_image(self.pawn3_w[0], anchor=NW, image=self.img_pawn3_w)
        self.img_pawn4_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn4_w.png')
        self.frame.create_image(self.pawn4_w[0], anchor=NW, image=self.img_pawn4_w)
        self.img_pawn5_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn5_w.png')
        self.frame.create_image(self.pawn5_w[0], anchor=NW, image=self.img_pawn5_w)
        self.img_pawn6_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn6_w.png')
        self.frame.create_image(self.pawn6_w[0], anchor=NW, image=self.img_pawn6_w)
        self.img_pawn7_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn7_w.png')
        self.frame.create_image(self.pawn7_w[0], anchor=NW, image=self.img_pawn7_w)
        self.img_pawn8_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn8_w.png')
        self.frame.create_image(self.pawn8_w[0], anchor=NW, image=self.img_pawn8_w)

        self.root.mainloop()

    def piece_position_update(self):

        self.piece_positions()

        for a in range(1, 17):

            print(self.white_pieces[a-1][0],self.white_pieces[a-1][1])

        self.root.mainloop()

data = ChessWorld()

# data.pieces()

data.board()

# data.pieces_list()

#data.piece_position_update()

# data.posval()