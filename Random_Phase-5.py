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
        self.white_choice = ()
        self.bc = (); self.bp = (); self.mp = ();
        self.Rb1 = (); self.Rb2 = (); self.Rw1 = (); self.Rw2 = (); self.Ktw1 = (); self.Ktw2 = (); self.Ktb1 = ();
        self.Ktb2 = (); self.Bw1 = (); self.Bw2 = (); self.Bb1 = (); self.Bb2 = (); self.Qw = (); self.Qb = ()
        self.Kw = (); self.Kb = (); self.Pb1 = (); self.Pb2 = (); self.Pb3 = (); self.Pb4 = (); self.Pb5 = ();
        self.Pb6 = (); self.Pb7 = (); self.Pb8 = (); self.Pw2 = (); self.Pw3 = (); self.Pw4 = (); self.Pw5 = ();
        self.Pw6 = (); self.Pw7 = (); self.Pw8 = (); self.Pw1 = ();
        np.array = []; self.white_pieces = []; self.black_pieces = []; self.move_vector = [];
        self.board_pieces = []; self.white_index_x = (); self.black_index_x = ();
        piece = []; self.white_hold = []; self.black_hold = []; self.white_move_vector = [];
        self.black_move_vector = []; self.move_white_agent = []
        self.move_black_agent = []; self.piece_move_vector = []
        self.white_piece_board_coords = []; self.black_piece_board_coords = []; self.potential_coords_vector = []

        # self.root.mainloop()

    def pieces(self):
#        self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Rw1', , 'Bw1', 'Qw',
 #                                  'Kw', 'Bw2', 'Ktw2', 'Rw2']
        self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8']

        # self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8', 'Rb1', 'Ktb1', 'Bb1', 'Qb',
         #                          'Kb', 'Bb2', 'Ktb2', 'Rb2']
        self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8']

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
        """bp = board_pieces"""
        self.bp = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.bp[0][0] = 'Rb1'; self.bp[0][1] = 'Ktb1'; self.bp[0][2] = 'Bb1'; self.bp[0][3] = 'Qb';
        self.bp[0][4] = 'Kb'; self.bp[0][5] = 'Bb2'; self.bp[0][6] = 'Ktb2'; self.bp[0][7] = 'Rb2'
        """row 7 coordinates"""
        self.bp[1][0] = 'Pb1'; self.bp[1][1] = 'Pb2'; self.bp[1][2] = 'Pb3'; self.bp[1][3] = 'Pb4';
        self.bp[1][4] = 'Pb5'; self.bp[1][5] = 'Pb6'; self.bp[1][6] = 'Pb7'; self.bp[1][7] = 'Pb8'
        """row 6 coordinates"""
        self.bp[2][0] = '   '; self.bp[2][1] = '   '; self.bp[2][2] = '   '; self.bp[2][3] = '   '
        self.bp[2][4] = '   '; self.bp[2][5] = '   '; self.bp[2][6] = '   '; self.bp[2][7] = '   '
        """row 5 coordinates"""
        self.bp[3][0] = '   '; self.bp[3][1] = '   '; self.bp[3][2] = '   '; self.bp[3][3] = '   '
        self.bp[3][4] = '   '; self.bp[3][5] = '   '; self.bp[3][6] = '   '; self.bp[3][7] = '   '
        """row 4 coordinates"""
        self.bp[4][0] = '   '; self.bp[4][1] = '   '; self.bp[4][2] = '   '; self.bp[4][3] = '   '
        self.bp[4][4] = '   '; self.bp[4][5] = '   '; self.bp[4][6] = '   '; self.bp[4][7] = '   '
        """row 3 coordinates"""
        self.bp[5][0] = '   '; self.bp[5][1] = '   '; self.bp[5][2] = '   '; self.bp[5][3] = '   '
        self.bp[5][4] = '   '; self.bp[5][5] = '   '; self.bp[5][6] = '   '; self.bp[5][7] = '   '
        """row 2 coordinates"""
        self.bp[6][0] = 'Pw1'; self.bp[6][1] = 'Pw2'; self.bp[6][2] = 'Pw3'; self.bp[6][3] = 'Pw4'
        self.bp[6][4] = 'Pw5'; self.bp[6][5] = 'Pw6'; self.bp[6][6] = 'Pw7'; self.bp[6][7] = 'Pw8'
        """row 1 coordinates"""
        self.bp[7][0] = 'Rw1'; self.bp[7][1] = 'Ktw1'; self.bp[7][2] = 'Bw1'; self.bp[7][3] = 'Qw'
        self.bp[7][4] = 'Kw'; self.bp[7][5] = 'Bw2'; self.bp[7][6] = 'Ktw2'; self.bp[7][7] = 'Rw2'
        """mp = move_matrix_pieces"""
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

        np.save('C:/Users/user/PycharmProjects/CHESS/Board_pieces', self.bp)
        np.save('C:/Users/user/PycharmProjects/CHESS/Board_coords', self.bc)
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
        self.bp[0][0] = self.frame.create_image(self.bc[0][0], anchor=NW, image=self.img_rook1_b)
        self.img_knight1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_b.png')
        self.bp[0][1] = self.frame.create_image(self.bc[0][1], anchor=NW, image=self.img_knight1_b)
        self.img_bishop1_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_b.png')
        self.bp[0][2] = self.frame.create_image(self.bc[0][2], anchor=NW, image=self.img_bishop1_b)
        self.img_queen_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b.png')
        self.bp[0][3] = self.frame.create_image(self.bc[0][3], anchor=NW, image=self.img_queen_b)
        self.img_king_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_b.png')
        self.bp[0][4] = self.frame.create_image(self.bc[0][4], anchor=NW, image=self.img_king_b)
        self.img_bishop2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_b.png')
        self.bp[0][5] = self.frame.create_image(self.bc[0][5], anchor=NW, image=self.img_bishop2_b)
        self.img_knight2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_b.png')
        self.bp[0][6] = self.frame.create_image(self.bc[0][6], anchor=NW, image=self.img_knight2_b)
        self.img_rook2_b = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_b.png')
        self.bp[0][7] = self.frame.create_image(self.bc[0][7], anchor=NW, image=self.img_rook2_b)
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
        self.bp[7][0] = self.frame.create_image(self.bc[7][0], anchor=NW, image=self.img_rook1_w)
        self.img_knight1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight1_w.png')
        self.bp[7][1] = self.frame.create_image(self.bc[7][1], anchor=NW, image=self.img_knight1_w)
        self.img_bishop1_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop1_w.png')
        self.bp[7][2] = self.frame.create_image(self.bc[7][2], anchor=NW, image=self.img_bishop1_w)
        self.img_queen_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w.png')
        self.bp[7][3] = self.frame.create_image(self.bc[7][3], anchor=NW, image=self.img_queen_w)
        self.img_king_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/king_w.png')
        self.bp[7][4] = self.frame.create_image(self.bc[7][4], anchor=NW, image=self.img_king_w)
        self.img_bishop2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/bishop2_w.png')
        self.bp[7][5] = self.frame.create_image(self.bc[7][5], anchor=NW, image=self.img_bishop2_w)
        self.img_knight2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/knight2_w.png')
        self.bp[7][6] = self.frame.create_image(self.bc[7][6], anchor=NW, image=self.img_knight2_w)
        self.img_rook2_w = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/rook2_w.png')
        self.bp[7][7] = self.frame.create_image(self.bc[7][7], anchor=NW, image=self.img_rook2_w)
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

        self.frame.update()
        #self.root.mainloop()

    def white_piece_vector(self):
        self.white_move_vector = []
        self.white_hold = []
        self.white_choice = np.random.randint(0, len(self.start_white_pieces))
        print('WHITE PIECE', self.start_white_pieces[self.white_choice])
        for i in range(0, 8):
            for j in range(0, 8):
                if self.mp[i][j] == self.start_white_pieces[self.white_choice]:
                    self.i_white_index = i
         #           print('index1', self.i_white_index)
                    self.j_white_index = j
          #          print('index2', self.j_white_index)
                    #print(self.mp[i][j])
                    self.white_piece_board_coords = self.bc[self.i_white_index][self.j_white_index]
           #         print('self.white_piece_board_coords', self.white_piece_board_coords)
                    if self.i_white_index == 6:
                        self.potential_coords_vector = [(self.bc[5][self.white_choice]), (self.bc[4][self.white_choice])]
                        self.potential_board_vector = [(self.mp[5][self.white_choice]), (self.mp[4][self.white_choice])]
                        if self.potential_board_vector[0] == '   ':
                            self.white_hold.append(self.potential_coords_vector[0])
                        if self.potential_board_vector[1] == '   ':
                            self.white_hold.append(self.potential_coords_vector[1])
                            self.white_move_vector.append(self.white_hold)
                            self.white_move_vector = self.white_move_vector[0]
                            print('WHITE', self.white_move_vector)
                    elif self.i_white_index == 7 and self.j_white_index == 1:
                        if self.start_white_pieces[self.white_choice] == 'Ktw1':
                            self.potential_coords_vector = [(self.bc[5][0]), (self.bc[5][2])]
                            # print(self.potential_coords_vector)
                            self.potential_board_vector = [(self.mp[5][0]), (self.mp[5][2])]
                            if self.potential_board_vector[0] == '   ':
                                self.white_hold.append(self.potential_coords_vector[0])
                            if self.potential_board_vector[1] == '   ':
                                # print('HOLD', self.white_hold)
                                self.white_hold.append(self.potential_coords_vector[1])
                                self.white_move_vector.append(self.white_hold)
                                self.white_move_vector = self.white_move_vector[0]
                                # print('1st white move vector', self.white_move_vector)
                    elif self.i_white_index == 7 and self.j_white_index == 6:
                        if self.start_white_pieces[self.white_choice] == 'Ktw2':
                            self.potential_coords_vector = [(self.bc[5][5]), (self.bc[5][7])]
                            # print(self.potential_coords_vector)
                            self.potential_board_vector = [(self.mp[5][5]), (self.mp[5][7])]
                            if self.potential_board_vector[0] == '   ':
                                self.white_hold.append(self.potential_coords_vector[0])
                            if self.potential_board_vector[1] == '   ':
                                # print('HOLD', self.white_hold)
                                self.white_hold.append(self.potential_coords_vector[1])
                                self.white_move_vector.append(self.white_hold)
                                self.white_move_vector = self.white_move_vector[0]
                                # print('1st white move vector', self.white_move_vector)

    def black_piece_vector(self):
        self.pieces()
        #self.board_data()
        self.black_move_vector = []
        self.black_hold = []
        self.black_choice = np.random.randint(0, len(self.start_black_pieces))
        print('BLACK PIECE', self.start_black_pieces[self.black_choice])
        for i in range(0, 8):
            for j in range(0, 8):
                if self.mp[i][j] == self.start_black_pieces[self.black_choice]:
                    self.i_black_index = i
                    self.j_black_index = j
                    self.black_piece_board_coords = self.bc[self.i_black_index][self.j_black_index]
                    if self.i_black_index == 1:
                        self.potential_coords_vector = [(self.bc[2][self.black_choice]),(self.bc[3][self.black_choice])]
                        self.potential_board_vector = [(self.mp[2][self.black_choice]), (self.mp[3][self.black_choice])]
                        if self.potential_board_vector[0] == '   ':
                            self.black_hold.append(self.potential_coords_vector[0])
                        if self.potential_board_vector[1] == '   ':
                            self.black_hold.append(self.potential_coords_vector[1])
                            self.black_move_vector.append(self.black_hold)
                            self.black_move_vector = self.black_move_vector[0]
                            print('BLACK', self.black_move_vector)
                    elif self.i_black_index == 0 and self.j_black_index == 1:
                        if self.start_black_pieces[self.black_choice] == 'Ktb1':
                            self.potential_coords_vector = [(self.bc[2][0]), (self.bc[2][2])]
                            # print(self.potential_coords_vector)
                            self.potential_board_vector = [(self.mp[2][0]), (self.mp[2][2])]
                            if self.potential_board_vector[0] == '   ':
                                self.black_hold.append(self.potential_coords_vector[0])
                            if self.potential_board_vector[1] == '   ':
                                # print('HOLD', self.white_hold)
                                self.black_hold.append(self.potential_coords_vector[1])
                                self.black_move_vector.append(self.black_hold)
                                self.black_move_vector = self.black_move_vector[0]
                                # print('1st white move vector', self.white_move_vector)
                    elif self.i_black_index == 0 and self.j_black_index == 6:
                        if self.start_black_pieces[self.black_choice] == 'Ktb2':
                            self.potential_coords_vector = [(self.bc[2][5]), (self.bc[2][7])]
                            # print(self.potential_coords_vector)
                            self.potential_board_vector = [(self.mp[2][5]), (self.mp[2][7])]
                            if self.potential_board_vector[0] == '   ':
                                self.black_hold.append(self.potential_coords_vector[0])
                            if self.potential_board_vector[1] == '   ':
                                # print('HOLD', self.white_hold)
                                self.black_hold.append(self.potential_coords_vector[1])
                                self.black_move_vector.append(self.black_hold)
                                self.black_move_vector = self.black_move_vector[0]
                                # print('1st white move vector', self.white_move_vector)

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

    def move_random_piece(self):
        self.pieces()
        self.board_data()
        self.board()
        time.sleep(1)
        for i in range(1, 3):
            self.white_piece_vector()
            self.black_piece_vector()
            self.white_board_label()
            print('')
            """select random move"""
            move = np.random.randint(0, len(self.white_move_vector))
            """MOVE piece"""
            random_piece_board_coords = self.white_move_vector[move]
            selection = random_piece_board_coords
            """define np move array"""
            zero = selection[0] - self.white_piece_board_coords[0]
            one = selection[1] - self.white_piece_board_coords[1]
            self.move_white_agent.append(zero)
            self.move_white_agent.append(one)
            """MOVE PIECE ON CHESS BOARD"""
            self.frame.move(self.agent, self.move_white_agent[0], self.move_white_agent[1])
            self.frame.update()
            self.move_white_agent = []
            time.sleep(1)
            """update piece matrix"""
            self.mp = np.load('C:/Users/user/PycharmProjects/CHESS/Move_piece.npy')
            for m in range(0, 8):
                for n in range(0, 8):
                    if self.bc[m][n] == random_piece_board_coords:
                        self.mp[m][n] == self.bc[m][n]
                        hold = self.mp[m][n]
                        self.mp[m][n] = self.mp[self.i_white_index][self.j_white_index]
                        self.mp[self.i_white_index][self.j_white_index] = hold
                        np.save('C:/Users/user/PycharmProjects/CHESS/Move_piece', self.mp)
                        print('white move', self.mp)
            self.black_board_label()
            move = np.random.randint(0, len(self.black_move_vector))
            """MOVE piece"""
            random_piece_board_coords = self.black_move_vector[move]
            selection = random_piece_board_coords
            """define np move array"""
            zero = selection[0] - self.black_piece_board_coords[0]
            one = selection[1] - self.black_piece_board_coords[1]
            self.move_black_agent.append(zero)
            self.move_black_agent.append(one)
            print('MOVE BLACK', self.move_black_agent)
            print('BLACK ZERO', self.move_black_agent[0])
            print('BLACK ONE', self.move_black_agent[1])
            """MOVE PIECE ON CHESS BOARD"""
            self.frame.move(self.agent, self.move_black_agent[0], self.move_black_agent[1])
            self.frame.update()
            time.sleep(1)
            """update piece matrix"""
            self.mp = np.load('C:/Users/user/PycharmProjects/CHESS/Move_piece.npy')
            self.move_black_agent = []
            """identify random move board piece data"""
            for r in range(0, 8):
                for s in range(0, 8):
                    if self.bc[r][s] == random_piece_board_coords:
                        self.mp[r][s] == self.bc[r][s]
                        hold = self.mp[r][s]
                        self.mp[r][s] = self.mp[self.i_black_index][self.j_black_index]
                        self.mp[self.i_black_index][self.j_black_index] = hold
                        print('')
                        hold = ()
                        np.save('C:/Users/user/PycharmProjects/CHESS/Move_piece', self.mp)
                        print(self.mp)

        self.root.mainloop()

data = ChessWorld()

#data.board()
#data.board_data()
#data.white_piece_vector()
#data.black_piece_vector()
#data.random_white_move()
data.move_random_piece()
#data.white_board_label()
#data.black_board_label()
