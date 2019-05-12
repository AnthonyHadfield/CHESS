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
        self.Rb1 = ();self.Rb2 = (); self.Rw1 = ();self.Rw2 = (); self.Ktw1 = (); self.Ktw2 = (); self.Ktb1 = ()
        self.Ktb2 = (); self.Bw1 = (); self.Bw2 = (); self.Bb1 = (); self.Bb2 = (); self.Qw = (); self.Qb = ()
        self.Kw = (); self.Kb = (); self.Pb1 = (); self.Pb2 = (); self.Pb3 = (); self.Pb4 = (); self.Pb5 = ();
        self.Pb6 = (); self.Pb7 = (); self.Pb8 = (); self.Pw1 = (); self.Pw2 = (); self.Pw3 = (); self.Pw4 = ();
        self.Pw5 = (); self.Pw6 = (); self.Pw7 = (); self.Pw8 = ()
        self.a1 = (); self.a2 = (); self.a3 = (); self.a4 = (); self.a5 = (); self.a6 = (); self.a7 = (); self.a8 = ()
        self.b1 = (); self.b2 = (); self.b3 = (); self.b4 = (); self.b5 = (); self.b6 = (); self.b7 = (); self.b8 = ()
        self.c1 = (); self.c2 = (); self.c3 = (); self.c4 = (); self.c5 = (); self.c6 = (); self.c7 = (); self.c8 = ()
        self.d1 = (); self.d2 = (); self.d3 = (); self.d4 = (); self.d5 = (); self.d6 = (); self.d7 = (); self.d8 = ()
        self.e1 = (); self.e2 = (); self.e3 = (); self.e4 = (); self.e5 = (); self.e6 = (); self.e7 = (); self.e8 = ()
        self.f1 = (); self.f2 = (); self.f3 = (); self.f4 = (); self.f5 = (); self.f6 = (); self.f7 = (); self.f8 = ()
        self.g1 = (); self.g2 = (); self.g3 = (); self.g4 = (); self.g5 = (); self.g6 = (); self.g7 = (); self.g8 = ()
        self.h1 = (); self.h2 = (); self.h3 = (); self.h4 = (); self.h5 = (); self.h6 = (); self.h7 = (); self.h8 = ()
        self.np = (); choice = (); zero_coord = ()
        Rb1 = self.Rb1; Rb2 = self.Rb2; Rw1 = self.Rw1; Rw2 = self.Rw2; Ktb1 = self.Ktb1; Ktb2 = self.Ktb2
        Ktw1 = self.Ktw1; Ktw2 = self.Ktw2; Bb1 = self.Bb1; Bb2 = self.Bb2; Bw1 = self.Bw1; Bw2 = self.Bw2
        Qb = self.Qb; Qw = self.Qw; Kb = self.Kb; Kw = self.Kw; Pb1 = self.Pb1; Pb2 = self.Pb2; Pb3 = self.Pb3;
        Pb4 = self.Pb4; Pb5 = self.Pb5; Pb6 = self.Pb6; Pb7 = self.Pb7; Pb8 = self.Pb8;
        Pw1 = self.Pw1; Pw2 = self.Pw2; Pw3 = self.Pw3; Pw4 = self.Pw4; Pw5 = self.Pw5;
        Pw6 = self.Pw6; Pw7 = self.Pw7; Pw8 = self.Pw8; self.Pw1_vector = []; np.array = []
        self.start_white_pieces = []
        self.start_black_pieces = []
        self.white_pieces = []; self.black_pieces = [];  self.board_vector = []; self.piece_vector = []
        self.no_piece_vector = []; self.current_position = (); self.agent = ();
        self.board_pieces = []

    def board_data(self):

        self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Rw1', 'Ktw1', 'Bw1', 'Qw',
                                   'Kw', 'Bw2', 'Ktw2', 'Rw2']
        self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8', 'Rb1', 'Ktb1', 'Bb1', 'Qb',
                                   'Kb', 'Bb2', 'Ktb2', 'Rb2']

        x = 8; y = 8
        """bc = board_coordinates"""
        self.bc = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.bc[0][0] = [34, 30]; self.bc[0][1] = [124, 30]; self.bc[0][2] = [214, 30]; self.bc[0][3] = [304, 30]
        self.bc[0][4] = [394, 30]; self.bc[0][5] = [484, 30]; self.bc[0][6] = [574, 30]; self.bc[0][7] = [646, 30]
        """row 7 coordinates"""
        self.bc[1][0] = [34, 118]; self.bc[1][1] = [124, 118]; self.bc[1][2] = [214, 118]; self.bc[1][3] = [304, 118]
        self.bc[1][4] = [394, 118]; self.bc[1][5] = [484, 118]; self.bc[1][6] = [574, 118]; self.bc[1][7] = [646, 118]
        """row 6 coordinates"""
        self.bc[2][0] = [34, 206]; self.bc[2][1] = [124, 206]; self.bc[2][2] = [214, 206]; self.bc[2][3] = [304, 206]
        self.bc[2][4] = [394, 206]; self.bc[2][5] = [484, 206]; self.bc[2][6] = [574, 206]; self.bc[2][7] = [646, 206]
        """row 5 coordinates"""
        self.bc[3][0] = [34, 294]; self.bc[3][1] = [124, 294]; self.bc[3][2] = [214, 294]; self.bc[3][3] = [304, 294]
        self.bc[3][4] = [394, 294]; self.bc[3][5] = [484, 294]; self.bc[3][6] = [574, 294]; self.bc[3][7] = [646, 294]
        """row 4 coordinates"""
        self.bc[4][0] = [34, 382]; self.bc[4][1] = [124, 382]; self.bc[4][2] = [214, 382]; self.bc[4][3] = [304, 382]
        self.bc[4][4] = [394, 382]; self.bc[4][5] = [484, 382]; self.bc[4][6] = [574, 382]; self.bc[4][7] = [646, 382]
        """row 3 coordinates"""
        self.bc[5][0] = [34, 470]; self.bc[5][1] = [124, 470]; self.bc[5][2] = [214, 470]; self.bc[5][3] = [304, 470]
        self.bc[5][4] = [394, 470]; self.bc[5][5] = [484, 470]; self.bc[5][6] = [574, 470]; self.bc[5][7] = [646, 470]
        """row 2 coordinates"""
        self.bc[6][0] = [34, 558]; self.bc[6][1] = [124, 558]; self.bc[6][2] = [214, 558]; self.bc[6][3] = [304, 558]
        self.bc[6][4] = [394, 558]; self.bc[6][5] = [484, 558]; self.bc[6][6] = [574, 558]; self.bc[6][7] = [646, 558]
        """row 1 coordinates"""
        self.bc[7][0] = [34, 646]; self.bc[7][1] = [124, 646]; self.bc[7][2] = [214, 646]; self.bc[7][3] = [304, 646]
        self.bc[7][4] = [394, 646]; self.bc[7][5] = [484, 646]; self.bc[7][6] = [574, 646]; self.bc[7][7] = [646, 646]
        """bp = board_pieces"""
        self.bp = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.bp[0][0] = 'Rb1'; self.bp[0][1] = 'Ktb1'; self.bp[0][2] = 'Bb1'; self.bp[0][3] = 'Qb'
        self.bp[0][4] = 'Kb'; self.bp[0][5] = 'Bb2'; self.bp[0][6] = 'Ktb2'; self.bp[0][7] = 'Rb2'
        """row 7 coordinates"""
        self.bp[1][0] = 'Pb1'; self.bp[1][1] = 'Pb2'; self.bp[1][2] = 'Pb3'; self.bp[1][3] = 'Pb4'
        self.bp[1][4] = 'Pb5'; self.bp[1][5] = 'Pb6'; self.bp[1][6] = 'Pb7'; self.bp[1][7] = 'Pb8'
        """row 6 coordinates"""
        self.bp[2][0] = '  '; self.bp[2][1] = '  '; self.bp[2][2] = '  '; self.bp[2][3] = '  '
        self.bp[2][4] = '  '; self.bp[2][5] = '  '; self.bp[2][6] = '  '; self.bp[2][7] = '  '
        """row 5 coordinates"""
        self.bp[3][0] = '  '; self.bp[3][1] = '  '; self.bp[3][2] = '  '; self.bp[3][3] = '  '
        self.bp[3][4] = '  '; self.bp[3][5] = '  '; self.bp[3][6] = '  '; self.bp[3][7] = '  '
        """row 4 coordinates"""
        self.bp[4][0] = '  '; self.bp[4][1] = '  '; self.bp[4][2] = '  '; self.bp[4][3] = '  '
        self.bp[4][4] = '  '; self.bp[4][5] = '  '; self.bp[4][6] = '  '; self.bp[4][7] = '  '
        """row 3 coordinates"""
        self.bp[5][0] = '  '; self.bp[5][1] = '  '; self.bp[5][2] = '  '; self.bp[5][3] = '  '
        self.bp[5][4] = '  '; self.bp[5][5] = '  '; self.bp[5][6] = '  '; self.bp[5][7] = '  '
        """row 2 coordinates"""
        self.bp[6][0] = 'Pw1'; self.bp[6][1] = 'Pw2'; self.bp[6][2] = 'Pw3'; self.bp[6][3] = 'Pw4'
        self.bp[6][4] = 'Pw5'; self.bp[6][5] = 'Pw6'; self.bp[6][6] = 'Pw7'; self.bp[6][7] = 'Pw8'
        """row 1 coordinates"""
        self.bp[7][0] = 'Rw1'; self.bp[7][1] = 'Ktw1'; self.bp[7][2] = 'Bw1'; self.bp[7][3] = 'Qw'
        self.bp[7][4] = 'Kw'; self.bp[7][5] = 'Bw2'; self.bp[7][6] = 'Ktw2'; self.bp[7][7] = 'Rw2'
        """bn = board_notation"""
        self.bn = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.bn[0][0] = 'a8'; self.bn[0][1] = 'b8'; self.bn[0][2] = 'c8'; self.bn[0][3] = 'd8'
        self.bn[0][4] = 'e8'; self.bn[0][5] = 'f8'; self.bn[0][6] = 'g8'; self.bn[0][7] = 'h8'
        """row 7 coordinates"""
        self.bn[1][0] = 'a7'; self.bn[1][1] = 'b7'; self.bn[1][2] = 'c7'; self.bn[1][3] = 'd7'
        self.bn[1][4] = 'e7'; self.bn[1][5] = 'f7'; self.bn[1][6] = 'g7'; self.bn[1][7] = 'h7'
        """row 6 coordinates"""
        self.bn[2][0] = 'a6'; self.bn[2][1] = 'b6'; self.bn[2][2] = 'c6'; self.bn[2][3] = 'd6'
        self.bn[2][4] = 'e6'; self.bn[2][5] = 'f6'; self.bn[2][6] = 'g6'; self.bn[2][7] = 'h6'
        """row 5 coordinates"""
        self.bn[3][0] = 'a5'; self.bn[3][1] = 'b5'; self.bn[3][2] = 'c5'; self.bn[3][3] = 'd5'
        self.bn[3][4] = 'e5'; self.bn[3][5] = 'f5'; self.bn[3][6] = 'g5'; self.bn[3][7] = 'h5'
        """row 4 coordinates"""
        self.bn[4][0] = 'a4'; self.bn[4][1] = 'b4'; self.bn[4][2] = 'c4'; self.bn[4][3] = 'd4'
        self.bn[4][4] = 'e4'; self.bn[4][5] = 'f4'; self.bn[4][6] = 'g4'; self.bn[4][7] = 'h4'
        """row 3 coordinates"""
        self.bn[5][0] = 'a3'; self.bn[5][1] = 'b3'; self.bn[5][2] = 'c3'; self.bn[5][3] = 'd3'
        self.bn[5][4] = 'e3'; self.bn[5][5] = 'f3'; self.bn[5][6] = 'g3'; self.bn[5][7] = 'h3'
        """row 2 coordinates"""
        self.bn[6][0] = 'a2'; self.bn[6][1] = 'b2'; self.bn[6][2] = 'c2'; self.bn[6][3] = 'd2'
        self.bn[6][4] = 'e2'; self.bn[6][5] = 'f2'; self.bn[6][6] = 'g2'; self.bn[6][7] = 'h2'
        """row 1 coordinates"""
        self.bn[7][0] = 'a1'; self.bn[7][1] = 'b1'; self.bn[7][2] = 'c1'; self.bn[7][3] = 'd1'
        self.bn[7][4] = 'e1'; self.bn[7][5] = 'f1'; self.bn[7][6] = 'g1'; self.bn[7][7] = 'h1'
        #np.save('C:/Users/user/PycharmProjects/CHESS/Board_pieces', self.bp)
        #
        #print('')
        #print(self.bp)
        #print('')
        #print(self.bc)
        #print(self.bn)
    def piece_files(self):
        self.board_data()
        for i in range(0, 8):
            for j in range(0, 8):
                self.board_pieces.append(self.bp[i][j])
        for i in range(0, len(self.start_white_pieces)):
            if self.start_white_pieces[i] in self.board_pieces:
                self.white_pieces.append(self.start_white_pieces[i])
        for i in range(0, len(self.start_black_pieces)):
            if self.start_black_pieces[i] in self.board_pieces:
                self.black_pieces.append(self.start_black_pieces[i])
    def board(self):
        self.board_data()
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
        Rb1 = self.frame.create_image(self.bc[0][0], anchor=NW, image=self.img_rook1_b)
        self.img_knight1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_b.png')
        Ktb1 = self.frame.create_image(self.bc[0][1], anchor=NW, image=self.img_knight1_b)
        self.img_bishop1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_b.png')
        Bb1 = self.frame.create_image(self.bc[0][2], anchor=NW, image=self.img_bishop1_b)
        self.img_queen_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b.png')
        Qb = self.frame.create_image(self.bc[0][3], anchor=NW, image=self.img_queen_b)
        self.img_king_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_b.png')
        Kb = self.frame.create_image(self.bc[0][4], anchor=NW, image=self.img_king_b)
        self.img_bishop2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_b.png')
        Bb2 = self.frame.create_image(self.bc[0][5], anchor=NW, image=self.img_bishop2_b)
        self.img_knight2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_b.png')
        Ktb2 = self.frame.create_image(self.bc[0][6], anchor=NW, image=self.img_knight2_b)
        self.img_rook2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_b.png')
        Rb2 = self.frame.create_image(self.bc[0][7], anchor=NW, image=self.img_rook2_b)
        self.img_pawn1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn1_b.png')
        Pb1 = self.frame.create_image(self.bc[1][0], anchor=NW, image=self.img_pawn1_b)
        self.img_pawn2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn2_b.png')
        self.frame.create_image(self.bc[1][1], anchor=NW, image=self.img_pawn2_b)
        self.img_pawn3_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn3_b.png')
        self.frame.create_image(self.bc[1][2], anchor=NW, image=self.img_pawn3_b)
        self.img_pawn4_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn4_b.png')
        self.frame.create_image(self.bc[1][3], anchor=NW, image=self.img_pawn4_b)
        self.img_pawn5_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn5_b.png')
        self.frame.create_image(self.bc[1][4], anchor=NW, image=self.img_pawn5_b)
        self.img_pawn6_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn6_b.png')
        self.frame.create_image(self.bc[1][5], anchor=NW, image=self.img_pawn6_b)
        self.img_pawn7_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn7_b.png')
        self.frame.create_image(self.bc[1][6], anchor=NW, image=self.img_pawn7_b)
        self.img_pawn8_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn8_b.png')
        self.frame.create_image(self.bc[1][7], anchor=NW, image=self.img_pawn8_b)
        """white pieces"""
        self.img_rook1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook1_w.png')
        self.frame.create_image(self.bc[7][0], anchor=NW, image=self.img_rook1_w)
        self.img_knight1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_w.png')
        self.frame.create_image(self.bc[7][1], anchor=NW, image=self.img_knight1_w)
        self.img_bishop1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_w.png')
        self.frame.create_image(self.bc[7][2], anchor=NW, image=self.img_bishop1_w)
        self.img_queen_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w.png')
        self.frame.create_image(self.bc[7][3], anchor=NW, image=self.img_queen_w)
        self.img_king_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_w.png')
        self.frame.create_image(self.bc[7][4], anchor=NW, image=self.img_king_w)
        self.img_bishop2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_w.png')
        self.frame.create_image(self.bc[7][5], anchor=NW, image=self.img_bishop2_w)
        self.img_knight2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_w.png')
        self.frame.create_image(self.bc[7][6], anchor=NW, image=self.img_knight2_w)
        self.img_rook2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_w.png')
        self.frame.create_image(self.bc[7][7], anchor=NW, image=self.img_rook2_w)
        self.img_pawn1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn1_w.png')
        self.agent = self.frame.create_image(self.bc[6][0], anchor=NW, image=self.img_pawn1_w)
        self.img_pawn2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn2_w.png')
        self.frame.create_image(self.bc[6][1], anchor=NW, image=self.img_pawn2_w)
        self.img_pawn3_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn3_w.png')
        self.frame.create_image(self.bc[6][2], anchor=NW, image=self.img_pawn3_w)
        self.img_pawn4_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn4_w.png')
        self.frame.create_image(self.bc[6][3], anchor=NW, image=self.img_pawn4_w)
        self.img_pawn5_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn5_w.png')
        self.frame.create_image(self.bc[6][4], anchor=NW, image=self.img_pawn5_w)
        self.img_pawn6_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn6_w.png')
        self.frame.create_image(self.bc[6][5], anchor=NW, image=self.img_pawn6_w)
        self.img_pawn7_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn7_w.png')
        self.frame.create_image(self.bc[6][6], anchor=NW, image=self.img_pawn7_w)
        self.img_pawn8_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/pawn8_w.png')
        self.frame.create_image(self.bc[6][7], anchor=NW, image=self.img_pawn8_w)
        self.frame.update()
        time.sleep(1)
    def move_piece(self):
        self.board()
        move_agent = np.array([0, -88])
        self.frame.move(self.agent, move_agent[0], move_agent[1])
        s = self.frame.coords(self.agent)
        #print(s)
        self.frame.update()
        self.root.mainloop()
    def select_random_move(self):
        self.piece_files()
        print('')
        """number of items in piece list"""
        #print('number of items in piece list',len(self.white_pieces))
        """select random number from white pices"""
        choice = np.random.randint(0, len(self.start_white_pieces))
        #print('piece ID number =', choice)
        """identify piece from list of pieces"""
        #print('piece selected = ',self.white_pieces[choice])
        """current board coordinates"""
        #for i in range(0, 8):
         #   for j in range(0, 8):
          #      if self.bp[i][j] == self.white_pieces[choice]:
           #         print('i =', i)
            #        print('j =', j)
             #       self.i_index = i
              #      self.j_index = j
        self.i_index = 6
        self.j_index = 0
        """identify boards piece from matrix coordinates"""
        print('checking the piece ID =', self.bp[self.i_index][self.j_index])
        "identify the piece position"
        print('selected piece position',self.bn[self.i_index][self.j_index] )
        print('identify piece board coordinates', self.bc[self.i_index][self.j_index])
    def move_random_piece(self):
        self.select_random_move()
        if self.bp[self.i_index][self.j_index] == 'Pw1':
            Pw1_potential_vector = [(self.bp[5][0]), (self.bp[4][0])]
            if Pw1_potential_vector[0] == '  ':
                self.Pw1_vector.append(self.bc[5][0])
            if Pw1_potential_vector[1] == '  ':
                self.Pw1_vector.append(self.bc[4][0])
                print('')
                print('POSSIBLE MOVES VECTOR',self.Pw1_vector)
        """select random move"""
        move = np.random.randint(0, len(self.Pw1_vector))
        print('RANDOM MOVE coords', self.Pw1_vector[move] )
        """MOVE piece"""
        piece_board_coords = self.bc[self.i_index][self.j_index]
        """piece to move index data"""
        print('GET PIECE INDEX DATA')
        print('piece board coords', piece_board_coords)
        zero_index_coord = piece_board_coords[0]
        print('piece zero index coord', zero_index_coord)
        one_index_coord = piece_board_coords[1]
        print('piece one index coord', one_index_coord)
        """MOVE TO index data"""
        print('')
        print('GET MOVE TO INDEX DATA')
        random_move_coords = self.Pw1_vector[move]
        print('Random move coords', random_move_coords)
        zero_random_coords = random_move_coords[0]
        print('zero RANDOM index coord', zero_random_coords)
        one_random_coords = random_move_coords[1]
        print('one RANDOM index coord', one_random_coords)
        move_array_zero_index = (zero_random_coords - zero_index_coord)
        print('Move array zero index', move_array_zero_index)
        move_array_one_index = (one_random_coords - one_index_coord)
        print('Move array one index', move_array_one_index)
        """define move agent array"""
        print('MOVE AGENT ARRAY')
        np.array.append(move_array_zero_index)
        np.array.append(move_array_one_index)
        move_agent = np.array
        print('move agent', move_agent)
        """MOVE PIECE ON CHESS BOARD"""
        self.board()
        self.frame.move(self.agent, move_agent[0], move_agent[1])
        self.frame.update()
        """update piece matrix"""
        start_piece_notation = self.bp[self.i_index][self.j_index]
        print('start piece notation',start_piece_notation)
        """identify random move board piece data"""
        for i in range(0, 8):
           for j in range(0, 8):
                if self.bc[i][j] == random_move_coords:
                    self.bp[i][j] == self.bc[i][j]
                    print('data',self.bp[i][j])
                    hold = self.bp[i][j]
                    self.bp[i][j] = self.bp[self.i_index][self.j_index]
                    print('update',self.bp[i][j])
                    self.bp[self.i_index][self.j_index] = hold
                    #print('board update', self.bp)

        self.root.mainloop()

data = ChessWorld()

#data.board()
#data.board_data()
#data.move_piece()
#data.piece_files()
#data.select_random_move()
data.move_random_piece()

