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
        self.move = ()
        self.move_white_agent = []
        self.move_black_agent = []
        self.white_move_vector = []
        self.white_board_vector = []
        self.potential_white_board_vector = []
        self.potential_coords_vector = []
        self.black_move_vector = []
        self.black_board_vector = []
        self.potential_black_board_vector = []
        self.potential_coords_vector = []
        self.selected_white_piece_coords = []
        self.i_white_index = ()
        self.j_white_index = ()
        self.selected_black_piece_coords = []
        self.i_black_index = ()
        self.j_black_index = ()
        self.white_choice = ()
        self.black_choice = ()
        self.index = []
        self.Qw2 = ()
        self.Qb2 = ()
        self.i_queen_index = ()
        self.j_queen_index = ()
        self.white = []
        self.black = []
        self.data = np.array
        self.white_candidate_vector = []
        self.black_candidate_vector = []
        self.white_candidate_board_vector = []
        self.white_candidate_move_vector = []
        self.black_candidate_board_vector = []
        self.black_candidate_move_vector = []
        self.white_board_vector_choice = []
        self.black_board_vector_choice = []
        self.random_piece_board_coords = []
        self.potential_white_pawn_index = []
        self.potential_black_pawn_index = []
        self.white_pawn_index = []
        self.black_pawn_index = []
        self.white_candidate_index_vector = []
        self.black_candidate_index_vector = []
        self.move_index = ()
        self.hold_index = []
        self.random_index = []
        self.piece_index = []
        self.len = ()
        # self.root.mainloop()
    def pieces(self):
        #self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Rw1', 'Ktw1', 'Bw1', 'Qw'
         #                          'Kw', 'Bw2', 'Ktw2', 'Rw2']
        #self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Ktw1', 'Ktw2']
        self.start_white_pieces = ['Pw1', 'Pw2', 'Pw3', 'Pw4', 'Pw5', 'Pw6', 'Pw7', 'Pw8', 'Rw1', 'Ktw1', 'Bw1',
                                   'Qw1', 'Bw2', 'Ktw2', 'Rw2']
        #self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8', 'Rb1', 'Ktb1', 'Bb1', 'Qb'
         #                          'Kb', 'Bb2', 'Ktb2', 'Rb2']
        self.start_black_pieces = ['Pb1', 'Pb2', 'Pb3', 'Pb4', 'Pb5', 'Pb6', 'Pb7', 'Pb8', 'Rb1', 'Ktb1', 'Bb1',
                                   'Qb1', 'Bb2', 'Ktb2', 'Rb2']
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
        self.mp[0][0] = 'Rb1'; self.mp[0][1] = 'Ktb1'; self.mp[0][2] = 'Bb1'; self.mp[0][3] = 'Qb1'
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
        self.mp[7][0] = 'Rw1'; self.mp[7][1] = 'Ktw1'; self.mp[7][2] = 'Bw1'; self.mp[7][3] = 'Qw1'
        self.mp[7][4] = 'Kw'; self.mp[7][5] = 'Bw2'; self.mp[7][6] = 'Ktw2'; self.mp[7][7] = 'Rw2'
        """bid = board identification"""
        self.bid = np.zeros([x, y], dtype=np.object)
        """row 8 coordinates"""
        self.bid[0][0] = 1 ; self.bid[0][1] = 2; self.bid[0][2] = 3; self.bid[0][3] = 4
        self.bid[0][4] = 5; self.bid[0][5] = 6; self.bid[0][6] = 7; self.bid[0][7] = 8
        """row 7 coordinates"""
        self.bid[1][0] = 9; self.bid[1][1] = 10; self.bid[1][2] = 11; self.bid[1][3] = 12
        self.bid[1][4] = 13; self.bid[1][5] = 14; self.bid[1][6] = 15; self.bid[1][7] = 16
        """row 6 coordinates"""
        self.bid[2][0] = 17; self.bid[2][1] = 17; self.bid[2][2] = 17; self.bid[2][3] = 17
        self.bid[2][4] = 17; self.bid[2][5] = 17; self.bid[2][6] = 17; self.bid[2][7] = 17
        """row 5 coordinates"""
        self.bid[3][0] = 17; self.bid[3][1] = 17; self.bid[3][2] = 17; self.bid[3][3] = 17
        self.bid[3][4] = 17; self.bid[3][5] = 17; self.bid[3][6] = 17; self.bid[3][7] = 17
        """row 4 coordinates"""
        self.bid[4][0] = 17; self.bid[4][1] = 17; self.bid[4][2] = 17; self.bid[4][3] = 17
        self.bid[4][4] = 17; self.bid[4][5] = 17; self.bid[4][6] = 17; self.bid[4][7] = 17
        """row 3 coordinates"""
        self.bid[5][0] = 17; self.bid[5][1] = 17; self.bid[5][2] = 17; self.bid[5][3] = 17
        self.bid[5][4] = 17; self.bid[5][5] = 17; self.bid[5][6] = 17; self.bid[5][7] = 17
        """row 2 coordinates"""
        self.bid[6][0] = 18; self.bid[6][1] = 19; self.bid[6][2] = 20; self.bid[6][3] = 21
        self.bid[6][4] = 22; self.bid[6][5] = 23; self.bid[6][6] = 24; self.bid[6][7] = 25
        """row 1 coordinates"""
        self.bid[7][0] = 26; self.bid[7][1] = 27; self.bid[7][2] = 28; self.bid[7][3] = 29
        self.bid[7][4] = 30; self.bid[7][5] = 31; self.bid[7][6] = 32; self.bid[7][7] = 33
        np.save('C:/Users/user/PycharmProjects/CHESS/Move_piece', self.mp)
    def data_array(self):
        """"""
        self.board_data()
        data_initial = []
        print('board data', self.bid)
        print(self.bid.shape)
        self.data =np.reshape(self.bid, (64, 1))
        print('data', self.data)
        print('data shape', self.data.shape)
        """NEW DATA"""
        self.bid[1][0] = 17; self.bid[3][0] = 9
        self.data2 = self.bid
        print('data2', self.data2)
        self.data2 = np.reshape(self.bid, (64, 1))
        print('data2', self.data2)
        """Append data arrays"""
        data_initial.append(self.data)
        data_initial.append(self.data2)
        print('append array', data_initial)
        """multi stack"""
        self.data = np.stack((data_initial), axis=0)
        print('stacked data', self.data)
        print('stacked data', self.data.shape)
        self.root.mainloop()
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
        self.img_queen_b1 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b1.png')
        self.Qb1 = self.frame.create_image(self.bc[0][3], anchor=NW, image=self.img_queen_b1)
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
        self.img_queen_w1 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w1.png')
        self.Qw1 = self.frame.create_image(self.bc[7][3], anchor=NW, image=self.img_queen_w1)
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

    def white_pawn(self, i, j):
        #print('WHITE PAWN')
        #print('')
        self.white_move_vector = []
        self.white_board_vector = []
        self.potential_white_board_vector = []
        self.potential_coords_vector = []
        self.index = []
        new_index = []
        self.potential_white_pawn_index = []
        self.piece_index = []
        if self.i_white_index == 6:

            self.piece_index = (self.i_white_index, self.j_white_index)

            self.potential_coords_vector = [(self.bc[5][self.j_white_index]), (self.bc[4][self.j_white_index])]
            self.potential_white_board_vector = [(self.mp[5][self.j_white_index]), (self.mp[4][self.j_white_index])]

            #self.potential_white_pawn_index = [[5, self.j_white_index], [4, self.j_white_index]]
            #self.white_pawn_index.append(self.potential_white_pawn_index)

            if self.potential_white_board_vector[0] == '   ':
                self.white_move_vector.append(self.potential_coords_vector[0])
                self.white_board_vector.append(self.potential_white_board_vector[0])

            if self.potential_white_board_vector[1] == '   ':
                self.white_move_vector.append(self.potential_coords_vector[1])
                self.white_board_vector.append(self.potential_white_board_vector[1])


            #print('Append', self.white_pawn_index)

            #print('white index', self.white_pawn_index)
            #print('white coords vector 6', self.white_move_vector)
            #print('')
        elif self.i_white_index < 6:
            #print('WHITE INDEX < 6', self.i_white_index)
            self.index = [[-1, -1], [-1, 0], [-1, 1]]
            #print('selected piece index', i, j)
            """define adjusted index"""
            for x in range(0, 3):
                self.index[x][0] = self.index[x][0] + i
                self.index[x][1] = self.index[x][1] + j
            #print('new index', self.index)
            """REMOVE LEFT"""
            if self.j_white_index == 0:
                self.index.pop(0)
             #   print('new popped index', self.index)
            """REMOVE RIGHT"""
            if self.j_white_index == 7:
                self.index.pop(2)
              #  print('new popped index', self.index)
            #print('final WHITE INDEX result', self.index)
            '''convert index to coords and piece'''
            for x in range(0, len(self.index)):
                coords = self.bc[self.index[x][0]][self.index[x][1]]
                vector = self.mp[self.index[x][0]][self.index[x][1]]
                self.potential_coords_vector.append(coords)
                self.potential_white_board_vector.append(vector)
            #print('WHITE VECTOR', self.potential_white_board_vector)
            #print('WHITE COORDS', self.potential_coords_vector)
            """define final WHITE move and board vectors"""
            """check if Pw1"""
            if len(self.potential_white_board_vector) == 2 and self.j_white_index == 0:
                if self.potential_white_board_vector[0] == '   ':
                        self.white_move_vector.append(self.potential_coords_vector[0])
                        self.white_board_vector.append(self.potential_white_board_vector[0])
                if self.potential_white_board_vector[1] != '   ':
                        piece = list(self.potential_white_board_vector[1])
             #           print('BLACK PIECE', piece)
                        for i in range(0, len(piece)):
                            if piece[i] == 'b':
                                self.white_move_vector.append(self.potential_coords_vector[1])
                                self.white_board_vector.append(self.potential_white_board_vector[1])

            """check if Pw8"""
            if len(self.potential_white_board_vector) == 2 and self.j_white_index == 7:
                if self.potential_white_board_vector[0] != '   ':
                    piece = list(self.potential_white_board_vector[0])
              #      print('WHITE PIECE', piece)
                    for i in range(0, len(piece)):
                        if piece[i] == 'b':
                            self.white_move_vector.append(self.potential_coords_vector[0])
                            self.white_board_vector.append(self.potential_white_board_vector[0])
                if self.potential_white_board_vector[1] == '   ':
                        self.white_move_vector.append(self.potential_coords_vector[1])
                        self.white_board_vector.append(self.potential_white_board_vector[1])
                #print(self.white_board_vector)

            if len(self.potential_white_board_vector) == 3:
                #print('')
               # print('THREE')
                #print('INDEX', self.index)
                #print('')
                if self.potential_white_board_vector[0] != '   ':
                    piece = list(self.potential_white_board_vector[0])
                 #   print('FIRST PIECE', piece)
                    for n in range(0, len(piece)):
                        if piece[n] == 'b':
                            self.white_move_vector.append(self.potential_coords_vector[0])
                            self.white_board_vector.append(self.potential_white_board_vector[0])
                            new_index.append(self.index[0])
                  #          print('new index 1', new_index)
                   #         print('vector',self.white_board_vector)
                if self.potential_white_board_vector[1] == '   ':
                    self.white_move_vector.append(self.potential_coords_vector[1])
                    self.white_board_vector.append(self.potential_white_board_vector[1])
                    new_index.append(self.index[1])
                    #print('new index 2', new_index)
                    #print('vector', self.white_board_vector)
                if self.potential_white_board_vector[2] != '   ':
                    piece = list(self.potential_white_board_vector[2])
                    #print('SECOND PIECE', piece)
                    for n in range(0, len(piece)):
                        if piece[n] == 'b':
                            self.white_move_vector.append(self.potential_coords_vector[2])
                            self.white_board_vector.append(self.potential_white_board_vector[2])
                            new_index.append(self.index[2])
                     #       print('final new index', new_index)
                      #      print('vector', self.white_board_vector)
            #print('PAWN')
            #print('CURRENT WHITE VECTOR', self.white_board_vector)
            #print('LEN', len(self.white_board_vector))
            #print('white coords vector', self.white_move_vector)
            #print('white board vector', self.white_board_vector)
            #print('')


    def black_pawn(self, i, j):
 #       print('BLACK PAWN')
        #print('')
        self.black_move_vector = []
        self.black_board_vector = []
        self.potential_black_board_vector = []
        self.potential_coords_vector = []
        new_index = []
        self.index = []
        self.piece_index = []
        if self.i_black_index == 1:

            self.piece_index = (self.i_black_index, self.j_black_index)

            self.potential_coords_vector = [(self.bc[2][self.j_black_index]), (self.bc[3][self.j_black_index])]
            self.potential_black_board_vector = [(self.mp[2][self.j_black_index]), (self.mp[3][self.j_black_index])]

            if self.potential_black_board_vector[0] == '   ':
                self.black_move_vector.append(self.potential_coords_vector[0])
                self.black_board_vector.append(self.potential_black_board_vector[0])

            if self.potential_black_board_vector[1] == '   ':
                self.black_move_vector.append(self.potential_coords_vector[1])
                self.black_board_vector.append(self.potential_black_board_vector[1])


          #  print('black coords vector 1', self.black_move_vector)
           # print('black board vector 1', self.black_board_vector)
        elif self.i_black_index > 1:
   #         print('BLACK INDEX', self.i_black_index)
            self.index = [[1, -1], [1, 0], [1, 1]]
    #        print('selected piece index', i, j)
            """define adjusted index"""
            for x in range(0, 3):
                self.index[x][0] = self.index[x][0] + i
                self.index[x][1] = self.index[x][1] + j
     #       print('new BLACK index', self.index)
            """REMOVE LEFT"""
            if self.j_black_index == 0:
                self.index.pop(0)
      #          print('new popped index', self.index)
            """REMOVE RIGHT"""
            if self.j_black_index == 7:
                self.index.pop(2)
       #         print('new popped index', self.index)
        #    print('final Black INDEX result', self.index)
            '''convert index to coords and piece'''
            for x in range(0, len(self.index)):
                coords = self.bc[self.index[x][0]][self.index[x][1]]
                vector = self.mp[self.index[x][0]][self.index[x][1]]
                self.potential_coords_vector.append(coords)
                self.potential_black_board_vector.append(vector)
         #   print('BLACK VECTOR', self.potential_black_board_vector)
          #  print('BLACK COORDS', self.potential_coords_vector)
            print('')
            """define final BLACK move and board vectors"""
            """check if Pb1"""
            if len(self.potential_black_board_vector) == 2 and self.j_black_index == 0:
           #     print('LEN 2')
                if self.potential_black_board_vector[0] == '   ':
                        self.black_move_vector.append(self.potential_coords_vector[0])
                        self.black_board_vector.append(self.potential_black_board_vector[0])
                if self.potential_black_board_vector[1] != '   ':
                    piece = list(self.potential_black_board_vector[1])
#                    print('WHITE PIECE', piece)
                    for i in range(0, len(piece)):
                        if piece[i] == 'w':
                            self.black_move_vector.append(self.potential_coords_vector[1])
                            self.black_board_vector.append(self.potential_black_board_vector[1])
            """check if Pb8"""
            if len(self.potential_black_board_vector) == 2 and self.j_black_index == 7:
                if self.potential_black_board_vector[0] != '   ':
                        piece = list(self.potential_black_board_vector[0])
 #                       print('BLACK PIECE', piece)
                        for i in range(0, len(piece)):
                            if piece[i] == 'w':
                                self.black_move_vector.append(self.potential_coords_vector[0])
                                self.black_board_vector.append(self.potential_black_board_vector[0])
                if self.potential_black_board_vector[1] == '   ':
                        self.black_move_vector.append(self.potential_coords_vector[1])
                        self.black_board_vector.append(self.potential_black_board_vector[1])
            if len(self.potential_black_board_vector) == 3:
                #print('')
  #              print('THREE')
   #             print('INDEX', self.index)
                if self.potential_black_board_vector[0] != '   ':
                    piece = list(self.potential_black_board_vector[0])
    #                print('FIRST PIECE', piece)
                    for n in range(0, len(piece)):
                        if piece[n] == 'w':
                            self.black_move_vector.append(self.potential_coords_vector[0])
                            self.black_board_vector.append(self.potential_black_board_vector[0])
                            new_index.append(self.index[0])
     #                       print('new index 1', new_index)
      #                      print('vector', self.black_board_vector)
                if self.potential_black_board_vector[1] == '   ':
                    self.black_move_vector.append(self.potential_coords_vector[1])
                    self.black_board_vector.append(self.potential_black_board_vector[1])
                    new_index.append(self.index[1])
       #             print('new index 2', new_index)
        #            print('vector', self.black_board_vector)
                if self.potential_black_board_vector[2] != '   ':
                    piece = list(self.potential_black_board_vector[2])
 #                   print('SECOND PIECE', piece)
                    for n in range(0, len(piece)):
                        if piece[n] == 'w':
                            self.black_move_vector.append(self.potential_coords_vector[2])
                            self.black_board_vector.append(self.potential_black_board_vector[2])
                            new_index.append(self.index[2])
  #                          print('final new index', new_index)
   #                         print('vector', self.black_board_vector)
    #            print('PAWN')
     #           print('CURRENT BLACK VECTOR', self.black_board_vector)
      #          print('LEN', len(self.black_board_vector))
                #print('black coords vector', self.black_move_vector)
        #        print('black board vector', self.black_board_vector)
         #       print('END')
                #print('')

    def white_knight(self, i, j):
        self.white_move_vector = []
        self.white_board_vector = []
        self.potential_white_board_vector = []
        self.potential_coords_vector = []
        self.piece_index = (self.i_white_index, self.j_white_index)

        index = [[1, -2], [-1, -2], [-2, 1], [-2, -1], [1, 2], [-1, 2], [2, 1], [2, -1]]
        #print('selected piece index', i, j)
        """define adjusted index"""
        for x in range(0, 8):
            index[x][0] = index[x][0] + i
            index[x][1] = index[x][1] + j
 #       print('new index', index)
        """define index position to be removed"""
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
  #      print('final WHITE INDEX result', index)
        '''convert index to coords and piece'''
        for x in range(0, len(index)):
            coords = self.bc[index[x][0]][index[x][1]]
            vector = self.mp[index[x][0]][index[x][1]]
            self.potential_coords_vector.append(coords)
            self.potential_white_board_vector.append(vector)
        """define final WHITE move and board vectors"""
        for x in range(0, len(index)):
            if self.potential_white_board_vector[x] != '   ':
                piece = list(self.potential_white_board_vector[x])
   #             print('PIECE', piece)
                for i in range(0, len(piece)):
                    if piece[i] == 'b':
                        self.white_move_vector.append(self.potential_coords_vector[x])
                        self.white_board_vector.append(self.potential_white_board_vector[x])
            elif self.potential_white_board_vector[x] == '   ':
                self.white_move_vector.append(self.potential_coords_vector[x])
                self.white_board_vector.append(self.potential_white_board_vector[x])

    def black_knight(self, i, j):
        self.black_board_vector = []
        self.black_move_vector = []
        self.potential_black_board_vector = []
        self.potential_coords_vector = []
        self.piece_index = (self.i_black_index, self.j_black_index)
        index = [[1, -2], [-1, -2], [-2, 1], [-2, -1], [1, 2], [-1, 2], [2, 1], [2, -1]]
        #print('selected piece index', i, j)
        """define adjusted index"""
        for x in range(0, 8):
            index[x][0] = index[x][0] + i
            index[x][1] = index[x][1] + j
#        #print('new index', index)
        """define index position to be removed"""
        remove1 = []
        """REMOVE DOWN"""
        for i in range(0, len(index)):
            if index[i][0] > 7:
                remove1.append(i)
        #print(remove1)
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
 #       print('final BLACK INDEX result', index)
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
  #      print('black coords vector', self.black_move_vector)
   #     print('black board vector', self.black_board_vector)
    #    print('END KNIGHT')
        #print('')
    def white_bishop(self, i , j):
#        print('WHITE BISHOP')
        #print('')
        self.white_move_vector = []
        self.white_board_vector = []
        potential_white_board_vector1 = []
        potential_white_board_vector2 = []
        potential_white_board_vector3 = []
        potential_white_board_vector4 = []
        potential_coords_vector1 = []
        potential_coords_vector2 = []
        potential_coords_vector3 = []
        potential_coords_vector4 = []
        new_potential_white_board_vector1 = []
        new_potential_white_board_vector2 = []
        new_potential_white_board_vector3 = []
        new_potential_white_board_vector4 = []
        new_potential_coords_vector1 = []
        new_potential_coords_vector2 = []
        new_potential_coords_vector3 = []
        new_potential_coords_vector4 = []
        new_potential_white_board_vector_list = []
        self.piece_index = (self.i_white_index, self.j_white_index)
        """up_left"""
        index1 = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
        """up_right"""
        index2 = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
        """down_left"""
        index3 = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
        """down_right"""
        index4 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
        #print('selected piece index', i, j)
        """define adjusted index1"""
        for x in range(0, 7):
            index1[x][0] = index1[x][0] + i
            index1[x][1] = index1[x][1] + j
 #       print('new index1', index1)
        """define adjusted index2"""
        for x in range(0, 7):
            index2[x][0] = index2[x][0] + i
            index2[x][1] = index2[x][1] + j
  #      print('new index2', index2)
        """define adjusted index3"""
        for x in range(0, 7):
            index3[x][0] = index3[x][0] + i
            index3[x][1] = index3[x][1] + j
   #     print('new index3', index3)
        """define adjusted index4"""
        for x in range(0, 7):
            index4[x][0] = index4[x][0] + i
            index4[x][1] = index4[x][1] + j
    #    print('new index4', index4)
        """define index position to be removed"""
        remove1 = []
        """REMOVE up_left"""
        for i in range(0, len(index1)):
            if index1[i][1] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove1 = []
        for i in range(0, len(index1)):
            if index1[i][0] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove2 = []
        """REMOVE up_right"""
        for i in range(0, len(index2)):
            if index2[i][1] > 7:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove2 = []
        for i in range(0, len(index2)):
            if index2[i][0] < 0:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove3 = []
        """REMOVE down_left"""
        for i in range(0, len(index3)):
            if index3[i][0] > 7:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove3 = []
        for i in range(0, len(index3)):
            if index3[i][1] < 0:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove4 = []
        """REMOVE down_right"""
        for i in range(0, len(index4)):
            if index4[i][1] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        remove4 = []
        for i in range(0, len(index4)):
            if index4[i][0] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        #print('')
#        print('final WHITE INDEX1 result', index1)
 #       print('final WHITE INDEX2 result', index2)
  #      print('final WHITE INDEX3 result', index3)
   #     print('final WHITE INDEX4 result', index4)
        #print('')
        '''convert index's to board vectors'''
        """board/coords vector1"""
        for x in range(0, len(index1)):
            board_vector1 = self.mp[index1[x][0]][index1[x][1]]
            potential_white_board_vector1.append(board_vector1)
            coords_vector1 = self.bc[index1[x][0]][index1[x][1]]
            potential_coords_vector1.append(coords_vector1)
        """board/ coords vector2"""
        for x in range(0, len(index2)):
            board_vector2 = self.mp[index2[x][0]][index2[x][1]]
            potential_white_board_vector2.append(board_vector2)
            coords_vector2 = self.bc[index2[x][0]][index2[x][1]]
            potential_coords_vector2.append(coords_vector2)
        """board/coords vector3"""
        for x in range(0, len(index3)):
            board_vector3 = self.mp[index3[x][0]][index3[x][1]]
            potential_white_board_vector3.append(board_vector3)
            coords_vector3 = self.bc[index3[x][0]][index3[x][1]]
            potential_coords_vector3.append(coords_vector3)
        """board/coords vector4"""
        for x in range(0, len(index4)):
            board_vector4 = self.mp[index4[x][0]][index4[x][1]]
            potential_white_board_vector4.append(board_vector4)
            coords_vector4 = self.bc[index4[x][0]][index4[x][1]]
            potential_coords_vector4.append(coords_vector4)
        #print('')
#        print('WHITE VECTOR1', potential_white_board_vector1)
 #       print('WHITE VECTOR2', potential_white_board_vector2)
  #      print('WHITE VECTOR3', potential_white_board_vector3)
   #     print('WHITE VECTOR4', potential_white_board_vector4)
        #print('')
        for i in range(0, len(potential_white_board_vector1)):

            if potential_white_board_vector1[i] == '   ':
                new_potential_white_board_vector1.append(potential_white_board_vector1[i])
                new_potential_coords_vector1.append(potential_coords_vector1[i])
            elif potential_white_board_vector1[i] != '   ':
                piece = list(potential_white_board_vector1[i])
    #            print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector1.append(potential_white_board_vector1[i])
                        new_potential_coords_vector1.append(potential_coords_vector1[i])
                break
        for i in range(0, len(potential_white_board_vector2)):

            if potential_white_board_vector2[i] == '   ':
                new_potential_white_board_vector2.append(potential_white_board_vector2[i])
                new_potential_coords_vector2.append(potential_coords_vector2[i])
            elif potential_white_board_vector2[i] != '   ':
                piece = list(potential_white_board_vector2[i])
#                print('PIECE2', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector2.append(potential_white_board_vector2[i])
                        new_potential_coords_vector2.append(potential_coords_vector2[i])
                break

        for i in range(0, len(potential_white_board_vector3)):

            if potential_white_board_vector3[i] == '   ':
                new_potential_white_board_vector3.append(potential_white_board_vector3[i])
                new_potential_coords_vector3.append(potential_coords_vector3[i])
            elif potential_white_board_vector3[i] != '   ':
                piece = list(potential_white_board_vector3[i])
#                print('PIECE3', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector3.append(potential_white_board_vector3[i])
                        new_potential_coords_vector3.append(potential_coords_vector3[i])
                break

        for i in range(0, len(potential_white_board_vector4)):

            if potential_white_board_vector4[i] == '   ':
                new_potential_white_board_vector4.append(potential_white_board_vector4[i])
                new_potential_coords_vector4.append(potential_coords_vector4[i])
            elif potential_white_board_vector4[i] != '   ':
                piece = list(potential_white_board_vector4[i])
 #               print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    if piece[n] == 'b':
                        new_potential_white_board_vector4.append(potential_white_board_vector4[i])
                        new_potential_coords_vector4.append(potential_coords_vector4[i])
                break


  #      print('NEW WHITE VECTOR1', new_potential_white_board_vector1)
   #     print('NEW WHITE VECTOR2', new_potential_white_board_vector2)
    #    print('NEW WHITE VECTOR3', new_potential_white_board_vector3)
     #   print('NEW WHITE VECTOR4', new_potential_white_board_vector4)
 #       print('')
        if new_potential_white_board_vector1 != []:
            new_potential_white_board_vector_list.append('one')
        if new_potential_white_board_vector2 != []:
            new_potential_white_board_vector_list.append('two')
        if new_potential_white_board_vector3 != []:
            new_potential_white_board_vector_list.append('three')
        if new_potential_white_board_vector4 != []:
            new_potential_white_board_vector_list.append('four')
      #      print('index list', new_potential_white_board_vector_list)
        "select random index vector"
        if new_potential_white_board_vector_list != []:
            number_choice = np.random.randint(0, len(new_potential_white_board_vector_list))
            selection = new_potential_white_board_vector_list[number_choice]
            if selection == 'one':
                self.white_board_vector = new_potential_white_board_vector1
                self.white_move_vector = new_potential_coords_vector1
            elif selection == 'two':
                self.white_board_vector = new_potential_white_board_vector2
                self.white_move_vector = new_potential_coords_vector2
            elif selection == 'three':
                self.white_board_vector = new_potential_white_board_vector3
                self.white_move_vector = new_potential_coords_vector3
            elif selection == 'four':
                self.white_board_vector = new_potential_white_board_vector4
                self.white_move_vector = new_potential_coords_vector4
  #      print('')
#        print('white board vector', self.white_board_vector)
 #       print('white coords vector', self.white_move_vector)
   #     print('')

    def black_bishop(self, i, j):
  #      print('BLACK BISHOP')
    #    print('')
        self.black_move_vector = []
        self.black_board_vector = []
        potential_black_board_vector1 = []
        potential_black_board_vector2 = []
        potential_black_board_vector3 = []
        potential_black_board_vector4 = []
        potential_coords_vector1 = []
        potential_coords_vector2 = []
        potential_coords_vector3 = []
        potential_coords_vector4 = []
        new_potential_black_board_vector1 = []
        new_potential_black_board_vector2 = []
        new_potential_black_board_vector3 = []
        new_potential_black_board_vector4 = []
        new_potential_coords_vector1 = []
        new_potential_coords_vector2 = []
        new_potential_coords_vector3 = []
        new_potential_coords_vector4 = []
        new_potential_black_board_vector_list = []
        self.piece_index = (self.i_black_index, self.j_black_index)
        """up_left"""
        index1 = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, - 6], [-7, -7]]
        """up_right"""
        index2 = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
        """down_left"""
        index3 = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
        """down_right"""
        index4 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
        """define adjusted index1"""
        for x in range(0, 7):
            index1[x][0] = index1[x][0] + i
            index1[x][1] = index1[x][1] + j
#        print('new index1', index1)
        """define adjusted index2"""
        for x in range(0, 7):
            index2[x][0] = index2[x][0] + i
            index2[x][1] = index2[x][1] + j
 #       print('new index2', index2)
        """define adjusted index3"""
        for x in range(0, 7):
            index3[x][0] = index3[x][0] + i
            index3[x][1] = index3[x][1] + j
  #      print('new index3', index3)
        """define adjusted index4"""
        for x in range(0, 7):
            index4[x][0] = index4[x][0] + i
            index4[x][1] = index4[x][1] + j
   #     print('new index4', index4)
        """define index position to be removed"""
        remove1 = []
        """REMOVE up_left"""
        for i in range(0, len(index1)):
            if index1[i][1] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove1 = []
        for i in range(0, len(index1)):
            if index1[i][0] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove2 = []
        """REMOVE up_right"""
        for i in range(0, len(index2)):
            if index2[i][1] > 7:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove2 = []
        for i in range(0, len(index2)):
            if index2[i][0] < 0:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove3 = []
        """REMOVE down_left"""
        for i in range(0, len(index3)):
            if index3[i][0] > 7:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove3 = []
        for i in range(0, len(index3)):
            if index3[i][1] < 0:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove4 = []
        """REMOVE down_right"""
        for i in range(0, len(index4)):
            if index4[i][1] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        remove4 = []
        for i in range(0, len(index4)):
            if index4[i][0] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
     #   print('')
    #    print('final BLACK INDEX1 result', index1)
     #   print('final BLACK INDEX2 result', index2)
      #  print('final BLACK INDEX3 result', index3)
       # print('final BLACK INDEX4 result', index4)
      #  print('')
        '''convert index's to board vectors'''
        """board/coords vector1"""
        for x in range(0, len(index1)):
            board_vector1 = self.mp[index1[x][0]][index1[x][1]]
            potential_black_board_vector1.append(board_vector1)
            coords_vector1 = self.bc[index1[x][0]][index1[x][1]]
            potential_coords_vector1.append(coords_vector1)
        """board/coords vector2"""
        for x in range(0, len(index2)):
            board_vector2 = self.mp[index2[x][0]][index2[x][1]]
            potential_black_board_vector2.append(board_vector2)
            coords_vector2 = self.bc[index2[x][0]][index2[x][1]]
            potential_coords_vector2.append(coords_vector2)
        """board/coords vector3"""
        for x in range(0, len(index3)):
            board_vector3 = self.mp[index3[x][0]][index3[x][1]]
            potential_black_board_vector3.append(board_vector3)
            coords_vector3 = self.bc[index3[x][0]][index3[x][1]]
            potential_coords_vector3.append(coords_vector3)
        """board/coords vector4"""
        for x in range(0, len(index4)):
            board_vector4 = self.mp[index4[x][0]][index4[x][1]]
            potential_black_board_vector4.append(board_vector4)
            coords_vector4 = self.bc[index4[x][0]][index4[x][1]]
            potential_coords_vector4.append(coords_vector4)
       # print('')
#        print('BLACK VECTOR1', potential_black_board_vector1)
 #       print('BLACK VECTOR2', potential_black_board_vector2)
  #      print('BLACK VECTOR3', potential_black_board_vector3)
   #     print('BLACK VECTOR4', potential_black_board_vector4)
        #print('')
        for i in range(0, len(potential_black_board_vector1)):
            if potential_black_board_vector1[i] != '   ':
                piece = list(potential_black_board_vector1[i])
    #            print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector1.append(potential_black_board_vector1[i])
                        new_potential_coords_vector1.append(potential_coords_vector1[i])
                break
            elif potential_black_board_vector1[i] == '   ':
                new_potential_black_board_vector1.append(potential_black_board_vector1[i])
                new_potential_coords_vector1.append(potential_coords_vector1[i])
        for i in range(0, len(potential_black_board_vector2)):
            if potential_black_board_vector2[i] != '   ':
                piece = list(potential_black_board_vector2[i])
     #           print('PIECE2', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector2.append(potential_black_board_vector2[i])
                        new_potential_coords_vector2.append(potential_coords_vector2[i])
                break
            elif potential_black_board_vector2[i] == '   ':
                new_potential_black_board_vector2.append(potential_black_board_vector2[i])
                new_potential_coords_vector2.append(potential_coords_vector2[i])
        for i in range(0, len(potential_black_board_vector3)):
            if potential_black_board_vector3[i] != '   ':
                piece = list(potential_black_board_vector3[i])
      #          print('PIECE3', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector3.append(potential_black_board_vector3[i])
                        new_potential_coords_vector3.append(potential_coords_vector3[i])
                break
            elif potential_black_board_vector3[i] == '   ':
                new_potential_black_board_vector3.append(potential_black_board_vector3[i])
                new_potential_coords_vector3.append(potential_coords_vector3[i])
        for i in range(0, len(potential_black_board_vector4)):
            if potential_black_board_vector4[i] != '   ':
                piece = list(potential_black_board_vector4[i])
       #         print('PIECE4', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector4.append(potential_black_board_vector4[i])
                        new_potential_coords_vector4.append(potential_coords_vector4[i])
                break
            elif potential_black_board_vector4[i] == '   ':
                new_potential_black_board_vector4.append(potential_black_board_vector4[i])
                new_potential_coords_vector4.append(potential_coords_vector4[i])
        #print('NEW BLACK VECTOR1', new_potential_black_board_vector1)
        #print('NEW BLACK VECTOR2', new_potential_black_board_vector2)
        #print('NEW BLACK VECTOR3', new_potential_black_board_vector3)
        #print('NEW BLACK VECTOR4', new_potential_black_board_vector4)
        #print('')
        if new_potential_black_board_vector1 != []:
            new_potential_black_board_vector_list.append('one')
        if new_potential_black_board_vector2 != []:
            new_potential_black_board_vector_list.append('two')
        if new_potential_black_board_vector3 != []:
            new_potential_black_board_vector_list.append('three')
        if new_potential_black_board_vector4 != []:
            new_potential_black_board_vector_list.append('four')
#        print('index list', new_potential_black_board_vector_list)
        "select random index vector"
        if new_potential_black_board_vector_list != []:
            number_choice = np.random.randint(0, len(new_potential_black_board_vector_list))
            selection = new_potential_black_board_vector_list[number_choice]
            if selection == 'one':
                self.black_board_vector = new_potential_black_board_vector1
                self.black_move_vector = new_potential_coords_vector1
            elif selection == 'two':
                self.black_board_vector = new_potential_black_board_vector2
                self.black_move_vector = new_potential_coords_vector2
            elif selection == 'three':
                self.black_board_vector = new_potential_black_board_vector3
                self.black_move_vector = new_potential_coords_vector3
            elif selection == 'four':
                self.black_board_vector = new_potential_black_board_vector4
                self.black_move_vector = new_potential_coords_vector4
        #print('')
 #       print('black board vector', self.black_board_vector)
  #      print('black coords vector', self.black_move_vector)
        #print('')

    def white_rook(self, i, j):
        #print('')
        #print('WHITE ROOK')
        #print('')
        self.white_move_vector = []
        self.white_board_vector = []
        potential_white_board_vector1 = []
        potential_white_board_vector2 = []
        potential_white_board_vector3 = []
        potential_white_board_vector4 = []
        potential_coords_vector1 = []
        potential_coords_vector2 = []
        potential_coords_vector3 = []
        potential_coords_vector4 = []
        new_potential_white_board_vector1 = []
        new_potential_white_board_vector2 = []
        new_potential_white_board_vector3 = []
        new_potential_white_board_vector4 = []
        new_potential_coords_vector1 = []
        new_potential_coords_vector2 = []
        new_potential_coords_vector3 = []
        new_potential_coords_vector4 = []
        new_potential_white_board_vector_list = []
        self.piece_index = (self.i_white_index, self.j_white_index)
        """up"""
        index1 = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
        """down"""
        index2 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
        """left"""
        index3 = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]
        """right"""
        index4 = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
#        print('selected piece index', i, j)
        """define adjusted index1"""
        for x in range(0, 7):
            index1[x][0] = index1[x][0] + i
            index1[x][1] = index1[x][1] + j
 #       print('new index1', index1)
        """define adjusted index2"""
        for x in range(0, 7):
            index2[x][0] = index2[x][0] + i
            index2[x][1] = index2[x][1] + j
  #      print('new index2', index2)
        """define adjusted index3"""
        for x in range(0, 7):
            index3[x][0] = index3[x][0] + i
            index3[x][1] = index3[x][1] + j
   #     print('new index3', index3)
        """define adjusted index4"""
        for x in range(0, 7):
            index4[x][0] = index4[x][0] + i
            index4[x][1] = index4[x][1] + j
    #    print('new index4', index4)
        """define index position to be removed"""
        remove1 = []
        """REMOVE up"""
        for i in range(0, len(index1)):
            if index1[i][0] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove2 = []
        """REMOVE down"""
        for i in range(0, len(index2)):
            if index2[i][0] > 7:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove3 = []
        """REMOVE left"""
        for i in range(0, len(index3)):
            if index3[i][1] < 0:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove4 = []
        """REMOVE right"""
        for i in range(0, len(index4)):
            if index4[i][1] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        remove4 = []
        #print('')
#        print('final WHITE INDEX1 result', index1)
 #       print('final WHITE INDEX2 result', index2)
  #      print('final WHITE INDEX3 result', index3)
   #     print('final WHITE INDEX4 result', index4)
        #print('')
        '''convert index's to board vectors'''
        """board/coords vector1"""
        for x in range(0, len(index1)):
            board_vector1 = self.mp[index1[x][0]][index1[x][1]]
            potential_white_board_vector1.append(board_vector1)
            coords_vector1 = self.bc[index1[x][0]][index1[x][1]]
            potential_coords_vector1.append(coords_vector1)
        """board/ coords vector2"""
        for x in range(0, len(index2)):
            board_vector2 = self.mp[index2[x][0]][index2[x][1]]
            potential_white_board_vector2.append(board_vector2)
            coords_vector2 = self.bc[index2[x][0]][index2[x][1]]
            potential_coords_vector2.append(coords_vector2)
        """board/coords vector3"""
        for x in range(0, len(index3)):
            board_vector3 = self.mp[index3[x][0]][index3[x][1]]
            potential_white_board_vector3.append(board_vector3)
            coords_vector3 = self.bc[index3[x][0]][index3[x][1]]
            potential_coords_vector3.append(coords_vector3)
        """board/coords vector4"""
        for x in range(0, len(index4)):
            board_vector4 = self.mp[index4[x][0]][index4[x][1]]
            potential_white_board_vector4.append(board_vector4)
            coords_vector4 = self.bc[index4[x][0]][index4[x][1]]
            potential_coords_vector4.append(coords_vector4)
        #print('')
        #print('WHITE VECTOR1', potential_white_board_vector1)
        #print('WHITE VECTOR2', potential_white_board_vector2)
        #print('WHITE VECTOR3', potential_white_board_vector3)
        #print('WHITE VECTOR4', potential_white_board_vector4)
        #print('')
        for i in range(0, len(potential_white_board_vector1)):

            if potential_white_board_vector1[i] == '   ':
                new_potential_white_board_vector1.append(potential_white_board_vector1[i])
                new_potential_coords_vector1.append(potential_coords_vector1[i])

            elif potential_white_board_vector1[i] != '   ':
                piece = list(potential_white_board_vector1[i])
    #            print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector1.append(potential_white_board_vector1[i])
                        new_potential_coords_vector1.append(potential_coords_vector1[i])
            break

        for i in range(0, len(potential_white_board_vector2)):

            if potential_white_board_vector2[i] == '   ':
                new_potential_white_board_vector2.append(potential_white_board_vector2[i])
                new_potential_coords_vector2.append(potential_coords_vector2[i])
            elif potential_white_board_vector2[i] != '   ':
                piece = list(potential_white_board_vector2[i])
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector2.append(potential_white_board_vector2[i])
                        new_potential_coords_vector2.append(potential_coords_vector2[i])
            break

        for i in range(0, len(potential_white_board_vector3)):

            if potential_white_board_vector3[i] == '   ':
                new_potential_white_board_vector3.append(potential_white_board_vector3[i])
                new_potential_coords_vector3.append(potential_coords_vector3[i])
            elif potential_white_board_vector3[i] != '   ':
                piece = list(potential_white_board_vector3[i])
 #               print('PIECE3', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector3.append(potential_white_board_vector3[i])
                        new_potential_coords_vector3.append(potential_coords_vector3[i])
            break

        for i in range(0, len(potential_white_board_vector4)):

            if potential_white_board_vector4[i] == '   ':
                new_potential_white_board_vector4.append(potential_white_board_vector4[i])
                new_potential_coords_vector4.append(potential_coords_vector4[i])

            elif potential_white_board_vector4[i] != '   ':
                piece = list(potential_white_board_vector4[i])
  #              print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_white_board_vector4.append(potential_white_board_vector4[i])
                        new_potential_coords_vector4.append(potential_coords_vector4[i])
            break
        #print('NEW WHITE VECTOR1', new_potential_white_board_vector1)
        #print('NEW WHITE VECTOR2', new_potential_white_board_vector2)
        #print('NEW WHITE VECTOR3', new_potential_white_board_vector3)
        #print('NEW WHITE VECTOR4', new_potential_white_board_vector4)
        #print('')
        if new_potential_white_board_vector1 != []:
            new_potential_white_board_vector_list.append('one')
        if new_potential_white_board_vector2 != []:
            new_potential_white_board_vector_list.append('two')
        if new_potential_white_board_vector3 != []:
            new_potential_white_board_vector_list.append('three')
        if new_potential_white_board_vector4 != []:
            new_potential_white_board_vector_list.append('four')
        #print('WHITE index list', new_potential_white_board_vector_list)
        "select random index vector"
        if new_potential_white_board_vector_list != []:
            number_choice = np.random.randint(0, len(new_potential_white_board_vector_list))
            selection = new_potential_white_board_vector_list[number_choice]
            if selection == 'one':
                self.white_board_vector = new_potential_white_board_vector1
                self.white_move_vector = new_potential_coords_vector1
            elif selection == 'two':
                self.white_board_vector = new_potential_white_board_vector2
                self.white_move_vector = new_potential_coords_vector2
            elif selection == 'three':
                self.white_board_vector = new_potential_white_board_vector3
                self.white_move_vector = new_potential_coords_vector3
            elif selection == 'four':
                self.white_board_vector = new_potential_white_board_vector4
                self.white_move_vector = new_potential_coords_vector4
         #   print('')
#            print('white board vector', self.white_board_vector)
 #           print('white coords vector', self.white_move_vector)
          #  print('')


    def black_rook(self, i, j):
        #print('BLACK ROOK')
        # print('')
        self.black_move_vector = []
        self.black_board_vector = []
        potential_black_board_vector1 = []
        potential_black_board_vector2 = []
        potential_black_board_vector3 = []
        potential_black_board_vector4 = []
        potential_coords_vector1 = []
        potential_coords_vector2 = []
        potential_coords_vector3 = []
        potential_coords_vector4 = []
        new_potential_black_board_vector1 = []
        new_potential_black_board_vector2 = []
        new_potential_black_board_vector3 = []
        new_potential_black_board_vector4 = []
        new_potential_coords_vector1 = []
        new_potential_coords_vector2 = []
        new_potential_coords_vector3 = []
        new_potential_coords_vector4 = []
        new_potential_black_board_vector_list = []
        self.piece_index = (self.i_black_index, self.j_black_index)
        """up"""
        index1 = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
        """down"""
        index2 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
        """left"""
        index3 = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]
        """right"""
        index4 = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
        #        print('selected piece index', i, j)
        """define adjusted index1"""
        for x in range(0, 7):
            index1[x][0] = index1[x][0] + i
            index1[x][1] = index1[x][1] + j
            #       print('new index1', index1)
        """define adjusted index2"""
        for x in range(0, 7):
            index2[x][0] = index2[x][0] + i
        index2[x][1] = index2[x][1] + j
        #      print('new index2', index2)
        """define adjusted index3"""
        for x in range(0, 7):
            index3[x][0] = index3[x][0] + i
            index3[x][1] = index3[x][1] + j
            #     print('new index3', index3)
        """define adjusted index4"""
        for x in range(0, 7):
            index4[x][0] = index4[x][0] + i
            index4[x][1] = index4[x][1] + j
            #    print('new index4', index4)
        """define index position to be removed"""
        remove1 = []
        """REMOVE up"""
        for i in range(0, len(index1)):
            if index1[i][0] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove2 = []
        """REMOVE down"""
        for i in range(0, len(index2)):
            if index2[i][0] > 7:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove3 = []
        """REMOVE left"""
        for i in range(0, len(index3)):
            if index3[i][1] < 0:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove4 = []
        """REMOVE right"""
        for i in range(0, len(index4)):
            if index4[i][1] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        remove4 = []
        # print('')
        #        print('final WHITE INDEX1 result', index1)
        #       print('final WHITE INDEX2 result', index2)
        #      print('final WHITE INDEX3 result', index3)
        #     print('final WHITE INDEX4 result', index4)
        # print('')
        '''convert index's to board vectors'''
        """board/coords vector1"""
        for x in range(0, len(index1)):
            board_vector1 = self.mp[index1[x][0]][index1[x][1]]
            potential_black_board_vector1.append(board_vector1)
            coords_vector1 = self.bc[index1[x][0]][index1[x][1]]
            potential_coords_vector1.append(coords_vector1)
        """board/ coords vector2"""
        for x in range(0, len(index2)):
            board_vector2 = self.mp[index2[x][0]][index2[x][1]]
            potential_black_board_vector2.append(board_vector2)
            coords_vector2 = self.bc[index2[x][0]][index2[x][1]]
            potential_coords_vector2.append(coords_vector2)
        """board/coords vector3"""
        for x in range(0, len(index3)):
            board_vector3 = self.mp[index3[x][0]][index3[x][1]]
            potential_black_board_vector3.append(board_vector3)
            coords_vector3 = self.bc[index3[x][0]][index3[x][1]]
            potential_coords_vector3.append(coords_vector3)
        """board/coords vector4"""
        for x in range(0, len(index4)):
            board_vector4 = self.mp[index4[x][0]][index4[x][1]]
            potential_black_board_vector4.append(board_vector4)
            coords_vector4 = self.bc[index4[x][0]][index4[x][1]]
            potential_coords_vector4.append(coords_vector4)
            # print('')
            #        print('WHITE VECTOR1', potential_white_board_vector1)
            #       print('WHITE VECTOR2', potential_white_board_vector2)
            #      print('WHITE VECTOR3', potential_white_board_vector3)
            #     print('WHITE VECTOR4', potential_white_board_vector4)
        # print('')
        for i in range(0, len(potential_black_board_vector1)):

            if potential_black_board_vector1[i] == '   ':
                new_potential_black_board_vector1.append(potential_black_board_vector1[i])
                new_potential_coords_vector1.append(potential_coords_vector1[i])

            elif potential_black_board_vector1[i] != '   ':
                piece = list(potential_black_board_vector1[i])
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_black_board_vector1.append(potential_black_board_vector1[i])
                        new_potential_coords_vector1.append(potential_coords_vector1[i])
            break

        for i in range(0, len(potential_black_board_vector2)):

            if potential_black_board_vector2[i] == '   ':
                new_potential_black_board_vector2.append(potential_black_board_vector2[i])
                new_potential_coords_vector2.append(potential_coords_vector2[i])
            elif potential_black_board_vector2[i] != '   ':
                piece = list(potential_black_board_vector2[i])
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_black_board_vector2.append(potential_black_board_vector2[i])
                        new_potential_coords_vector2.append(potential_coords_vector2[i])
            break

        for i in range(0, len(potential_black_board_vector3)):

            if potential_black_board_vector3[i] == '   ':
                new_potential_black_board_vector3.append(potential_black_board_vector3[i])
                new_potential_coords_vector3.append(potential_coords_vector3[i])

            elif potential_black_board_vector3[i] != '   ':
                piece = list(potential_black_board_vector3[i])
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_black_board_vector3.append(potential_black_board_vector3[i])
                        new_potential_coords_vector3.append(potential_coords_vector3[i])
            break

        for i in range(0, len(potential_black_board_vector4)):

            if potential_black_board_vector4[i] == '   ':
                new_potential_black_board_vector4.append(potential_black_board_vector4[i])
                new_potential_coords_vector4.append(potential_coords_vector4[i])
            elif potential_black_board_vector4[i] != '   ':
                piece = list(potential_black_board_vector4[i])
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        break
                    elif piece[n] == 'b':
                        new_potential_black_board_vector4.append(potential_black_board_vector4[i])
                        new_potential_coords_vector4.append(potential_coords_vector4[i])
                break

                #    print('NEW WHITE VECTOR1', new_potential_white_board_vector1)
                #   print('NEW WHITE VECTOR2', new_potential_white_board_vector2)
                #  print('NEW WHITE VECTOR3', new_potential_white_board_vector3)
                # print('NEW WHITE VECTOR4', new_potential_white_board_vector4)
        # print('')
        if new_potential_black_board_vector1 != []:
            new_potential_black_board_vector_list.append('one')
        if new_potential_black_board_vector2 != []:
            new_potential_black_board_vector_list.append('two')
        if new_potential_black_board_vector3 != []:
            new_potential_black_board_vector_list.append('three')
        if new_potential_black_board_vector4 != []:
            new_potential_black_board_vector_list.append('four')
        #print('black index list', new_potential_black_board_vector_list)
        "select random index vector"

        if new_potential_black_board_vector_list != []:
            number_choice = np.random.randint(0, len(new_potential_black_board_vector_list))
            selection = new_potential_black_board_vector_list[number_choice]
            if selection == 'one':
                self.white_board_vector = new_potential_black_board_vector1
                self.white_move_vector = new_potential_coords_vector1
            elif selection == 'two':
                self.white_board_vector = new_potential_black_board_vector2
                self.white_move_vector = new_potential_coords_vector2
            elif selection == 'three':
                self.white_board_vector = new_potential_black_board_vector3
                self.white_move_vector = new_potential_coords_vector3
            elif selection == 'four':
                self.white_board_vector = new_potential_black_board_vector4
                self.white_move_vector = new_potential_coords_vector4
                #   print('')
                #            print('white board vector', self.white_board_vector)
                #           print('white coords vector', self.white_move_vector)
                #  print('')
        #print('HERE')
    def white_queen(self, i, j):
   #     print('WHITE QUEEN')
   #     print('')
        self.white_move_vector = []
        self.white_board_vector = []
        potential_white_board_vector1 = []
        potential_white_board_vector2 = []
        potential_white_board_vector3 = []
        potential_white_board_vector4 = []
        potential_white_board_vector5 = []
        potential_white_board_vector6 = []
        potential_white_board_vector7 = []
        potential_white_board_vector8 = []
        potential_coords_vector1 = []
        potential_coords_vector2 = []
        potential_coords_vector3 = []
        potential_coords_vector4 = []
        potential_coords_vector5 = []
        potential_coords_vector6 = []
        potential_coords_vector7 = []
        potential_coords_vector8 = []
        new_potential_white_board_vector1 = []
        new_potential_white_board_vector2 = []
        new_potential_white_board_vector3 = []
        new_potential_white_board_vector4 = []
        new_potential_white_board_vector5 = []
        new_potential_white_board_vector6 = []
        new_potential_white_board_vector7 = []
        new_potential_white_board_vector8 = []
        new_potential_coords_vector1 = []
        new_potential_coords_vector2 = []
        new_potential_coords_vector3 = []
        new_potential_coords_vector4 = []
        new_potential_coords_vector5 = []
        new_potential_coords_vector6 = []
        new_potential_coords_vector7 = []
        new_potential_coords_vector8 = []
        new_potential_white_board_vector_list = []
        self.piece_index = (self.i_white_index, self.j_white_index)

        """up"""
        index1 = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
        """down"""
        index2 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
        """left"""
        index3 = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]
        """right"""
        index4 = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
        """up_left"""
        index5 = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
        """up_right"""
        index6 = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
        """down_left"""
        index7 = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
        """down_right"""
        index8 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
#        print('selected piece index', i, j)
        """define adjusted index1"""
        for x in range(0, 7):
            index1[x][0] = index1[x][0] + i
            index1[x][1] = index1[x][1] + j
    #    print('new index1', index1)
        """define adjusted index2"""
        for x in range(0, 7):
            index2[x][0] = index2[x][0] + i
            index2[x][1] = index2[x][1] + j
     #   print('new index2', index2)
        """define adjusted index3"""
        for x in range(0, 7):
            index3[x][0] = index3[x][0] + i
            index3[x][1] = index3[x][1] + j
      #  print('new index3', index3)
        """define adjusted index4"""
        for x in range(0, 7):
            index4[x][0] = index4[x][0] + i
            index4[x][1] = index4[x][1] + j
       # print('new index4', index4)
        for x in range(0, 7):
            index5[x][0] = index5[x][0] + i
            index5[x][1] = index5[x][1] + j
 #       print('new index1', index5)
        """define adjusted index2"""
        for x in range(0, 7):
            index6[x][0] = index6[x][0] + i
            index6[x][1] = index6[x][1] + j
  #      print('new index6', index6)
        """define adjusted index3"""
        for x in range(0, 7):
            index7[x][0] = index7[x][0] + i
            index7[x][1] = index7[x][1] + j
   #     print('new index7', index7)
        """define adjusted index4"""
        for x in range(0, 7):
            index8[x][0] = index8[x][0] + i
            index8[x][1] = index8[x][1] + j
    #    print('new index8', index8)
        """define index position to be removed"""
        remove1 = []
        """REMOVE up"""
        for i in range(0, len(index1)):
            if index1[i][0] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove2 = []
        """REMOVE down"""
        for i in range(0, len(index2)):
            if index2[i][0] > 7:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove3 = []
        """REMOVE left"""
        for i in range(0, len(index3)):
            if index3[i][1] < 0:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove4 = []
        """REMOVE right"""
        for i in range(0, len(index4)):
            if index4[i][1] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        remove5 = []
        """REMOVE up_left"""
        for i in range(0, len(index5)):
            if index5[i][1] < 0:
                remove5.append(i)
        for i in range(0, len(remove5)):
            index5.pop(remove5[i] - i)
        remove5 = []
        for i in range(0, len(index5)):
            if index5[i][0] < 0:
                remove5.append(i)
        for i in range(0, len(remove5)):
            index5.pop(remove5[i] - i)
        remove6 = []
        """REMOVE up_right"""
        for i in range(0, len(index6)):
            if index6[i][1] > 7:
                remove6.append(i)
        for i in range(0, len(remove6)):
            index6.pop(remove6[i] - i)
        remove6 = []
        for i in range(0, len(index6)):
            if index6[i][0] < 0:
                remove6.append(i)
        for i in range(0, len(remove6)):
            index6.pop(remove6[i] - i)
        remove7 = []
        """REMOVE down_left"""
        for i in range(0, len(index7)):
            if index7[i][0] > 7:
                remove7.append(i)
        for i in range(0, len(remove7)):
            index7.pop(remove7[i] - i)
        remove7 = []
        for i in range(0, len(index7)):
            if index7[i][1] < 0:
                remove7.append(i)
        for i in range(0, len(remove7)):
            index7.pop(remove7[i] - i)
        remove8 = []
        """REMOVE down_right"""
        for i in range(0, len(index8)):
            if index8[i][1] > 7:
                remove8.append(i)
        for i in range(0, len(remove8)):
            index8.pop(remove8[i] - i)
        remove8 = []
        for i in range(0, len(index8)):
            if index8[i][0] > 7:
                remove8.append(i)
        for i in range(0, len(remove8)):
            index8.pop(remove8[i] - i)
      #  print('')
     #   print('final WHITE INDEX1 result', index1)
       # print('final WHITE INDEX2 result', index2)
        #print('final WHITE INDEX3 result', index3)
#        print('final WHITE INDEX4 result', index4)
 #       print('final WHITE INDEX5 result', index5)
  #      print('final WHITE INDEX6 result', index6)
   #     print('final WHITE INDEX7 result', index7)
    #    print('final WHITE INDEX8 result', index8)
 #       print('')
        '''convert index's to board vectors'''
        """board/coords vector1"""
        for x in range(0, len(index1)):
            board_vector1 = self.mp[index1[x][0]][index1[x][1]]
            potential_white_board_vector1.append(board_vector1)
            coords_vector1 = self.bc[index1[x][0]][index1[x][1]]
            potential_coords_vector1.append(coords_vector1)
        """board/ coords vector2"""
        for x in range(0, len(index2)):
            board_vector2 = self.mp[index2[x][0]][index2[x][1]]
            potential_white_board_vector2.append(board_vector2)
            coords_vector2 = self.bc[index2[x][0]][index2[x][1]]
            potential_coords_vector2.append(coords_vector2)
        """board/coords vector3"""
        for x in range(0, len(index3)):
            board_vector3 = self.mp[index3[x][0]][index3[x][1]]
            potential_white_board_vector3.append(board_vector3)
            coords_vector3 = self.bc[index3[x][0]][index3[x][1]]
            potential_coords_vector3.append(coords_vector3)
        """board/coords vector4"""
        for x in range(0, len(index4)):
            board_vector4 = self.mp[index4[x][0]][index4[x][1]]
            potential_white_board_vector4.append(board_vector4)
            coords_vector4 = self.bc[index4[x][0]][index4[x][1]]
            potential_coords_vector4.append(coords_vector4)
        """board/ coords vector5"""
        for x in range(0, len(index5)):
            board_vector5 = self.mp[index5[x][0]][index5[x][1]]
            potential_white_board_vector5.append(board_vector5)
            coords_vector5 = self.bc[index5[x][0]][index5[x][1]]
            potential_coords_vector5.append(coords_vector5)
        """board/ coords vector6"""
        for x in range(0, len(index6)):
            board_vector6 = self.mp[index6[x][0]][index6[x][1]]
            potential_white_board_vector6.append(board_vector6)
            coords_vector6 = self.bc[index6[x][0]][index6[x][1]]
            potential_coords_vector6.append(coords_vector6)
        """board/coords vector7"""
        for x in range(0, len(index7)):
            board_vector7 = self.mp[index7[x][0]][index7[x][1]]
            potential_white_board_vector7.append(board_vector7)
            coords_vector7 = self.bc[index7[x][0]][index7[x][1]]
            potential_coords_vector7.append(coords_vector7)
        """board/coords vector8"""
        for x in range(0, len(index8)):
            board_vector8 = self.mp[index8[x][0]][index8[x][1]]
            potential_white_board_vector8.append(board_vector8)
            coords_vector8 = self.bc[index8[x][0]][index8[x][1]]
            potential_coords_vector8.append(coords_vector8)
  #      print('')
     #   print('WHITE VECTOR1', potential_white_board_vector1)
      #  print('WHITE VECTOR2', potential_white_board_vector2)
       # print('WHITE VECTOR3', potential_white_board_vector3)
        #print('WHITE VECTOR4', potential_white_board_vector4)
 #       print('WHITE VECTOR5', potential_white_board_vector5)
  #      print('WHITE VECTOR6', potential_white_board_vector6)
   #     print('WHITE VECTOR7', potential_white_board_vector7)
    #    print('WHITE VECTOR8', potential_white_board_vector8)
   #     print('')
        for i in range(0, len(potential_white_board_vector1)):
            if potential_white_board_vector1[i] != '   ':
                piece = list(potential_white_board_vector1[i])
     #           print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector1.append(potential_white_board_vector1[i])
                        new_potential_coords_vector1.append(potential_coords_vector1[i])
                break
            elif potential_white_board_vector1[i] == '   ':
                new_potential_white_board_vector1.append(potential_white_board_vector1[i])
                new_potential_coords_vector1.append(potential_coords_vector1[i])

        for i in range(0, len(potential_white_board_vector2)):
            if potential_white_board_vector2[i] != '   ':
                piece = list(potential_white_board_vector2[i])
      #          print('PIECE2', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector2.append(potential_white_board_vector2[i])
                        new_potential_coords_vector2.append(potential_coords_vector2[i])
                break
            elif potential_white_board_vector2[i] == '   ':
                new_potential_white_board_vector2.append(potential_white_board_vector2[i])
                new_potential_coords_vector2.append(potential_coords_vector2[i])
        for i in range(0, len(potential_white_board_vector3)):
            if potential_white_board_vector3[i] != '   ':
                piece = list(potential_white_board_vector3[i])
       #         print('PIECE3', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector3.append(potential_white_board_vector3[i])
                        new_potential_coords_vector3.append(potential_coords_vector3[i])
                break
            elif potential_white_board_vector3[i] == '   ':
                new_potential_white_board_vector3.append(potential_white_board_vector3[i])
                new_potential_coords_vector3.append(potential_coords_vector3[i])
        for i in range(0, len(potential_white_board_vector4)):
            if potential_white_board_vector4[i] != '   ':
                piece = list(potential_white_board_vector4[i])
#                print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector4.append(potential_white_board_vector4[i])
                        new_potential_coords_vector4.append(potential_coords_vector4[i])
                break
            elif potential_white_board_vector4[i] == '   ':
                new_potential_white_board_vector4.append(potential_white_board_vector4[i])
                new_potential_coords_vector4.append(potential_coords_vector4[i])
        for i in range(0, len(potential_white_board_vector5)):
            if potential_white_board_vector5[i] != '   ':
                piece = list(potential_white_board_vector5[i])
 #               print('PIECE5', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector5.append(potential_white_board_vector5[i])
                        new_potential_coords_vector5.append(potential_coords_vector5[i])
                break
            elif potential_white_board_vector5[i] == '   ':
                new_potential_white_board_vector5.append(potential_white_board_vector5[i])
                new_potential_coords_vector5.append(potential_coords_vector5[i])
        for i in range(0, len(potential_white_board_vector6)):
            if potential_white_board_vector6[i] != '   ':
                piece = list(potential_white_board_vector6[i])
  #              print('PIECE6', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector6.append(potential_white_board_vector6[i])
                        new_potential_coords_vector6.append(potential_coords_vector6[i])
                break
            elif potential_white_board_vector6[i] == '   ':
                new_potential_white_board_vector6.append(potential_white_board_vector6[i])
                new_potential_coords_vector6.append(potential_coords_vector6[i])
        for i in range(0, len(potential_white_board_vector7)):
            if potential_white_board_vector7[i] != '   ':
                piece = list(potential_white_board_vector7[i])
   #             print('PIECE7', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector7.append(potential_white_board_vector7[i])
                        new_potential_coords_vector7.append(potential_coords_vector7[i])
                break
            elif potential_white_board_vector7[i] == '   ':
                new_potential_white_board_vector7.append(potential_white_board_vector7[i])
                new_potential_coords_vector7.append(potential_coords_vector7[i])
        for i in range(0, len(potential_white_board_vector8)):
            if potential_white_board_vector8[i] != '   ':
                piece = list(potential_white_board_vector8[i])
    #            print('PIECE8', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'b':
                        new_potential_white_board_vector8.append(potential_white_board_vector8[i])
                        new_potential_coords_vector8.append(potential_coords_vector8[i])
                break
            elif potential_white_board_vector8[i] == '   ':
                new_potential_white_board_vector8.append(potential_white_board_vector8[i])
                new_potential_coords_vector8.append(potential_coords_vector8[i])
 #       print('NEW WHITE VECTOR1', new_potential_white_board_vector1)
  #      print('NEW WHITE VECTOR2', new_potential_white_board_vector2)
   #     print('NEW WHITE VECTOR3', new_potential_white_board_vector3)
    #    print('NEW WHITE VECTOR4', new_potential_white_board_vector4)
     #   print('NEW WHITE VECTOR5', new_potential_white_board_vector5)
      #  print('NEW WHITE VECTOR6', new_potential_white_board_vector6)
       # print('NEW WHITE VECTOR7', new_potential_white_board_vector7)
        #print('NEW WHITE VECTOR8', new_potential_white_board_vector8)
        #print('')
        if new_potential_white_board_vector1 != []:
            new_potential_white_board_vector_list.append('one')
        if new_potential_white_board_vector2 != []:
            new_potential_white_board_vector_list.append('two')
        if new_potential_white_board_vector3 != []:
            new_potential_white_board_vector_list.append('three')
        if new_potential_white_board_vector4 != []:
            new_potential_white_board_vector_list.append('four')
        if new_potential_white_board_vector5 != []:
            new_potential_white_board_vector_list.append('five')
        if new_potential_white_board_vector6 != []:
            new_potential_white_board_vector_list.append('six')
        if new_potential_white_board_vector7 != []:
            new_potential_white_board_vector_list.append('seven')
        if new_potential_white_board_vector8 != []:
            new_potential_white_board_vector_list.append('eight')
#            print('index list', new_potential_white_board_vector_list)
        "select random index vector"
        if new_potential_white_board_vector_list != []:
            number_choice = np.random.randint(0, len(new_potential_white_board_vector_list))
            selection = new_potential_white_board_vector_list[number_choice]
            if selection == 'one':
                self.white_board_vector = new_potential_white_board_vector1
                self.white_move_vector = new_potential_coords_vector1
            elif selection == 'two':
                self.white_board_vector = new_potential_white_board_vector2
                self.white_move_vector = new_potential_coords_vector2
            elif selection == 'three':
                self.white_board_vector = new_potential_white_board_vector3
                self.white_move_vector = new_potential_coords_vector3
            elif selection == 'four':
                self.white_board_vector = new_potential_white_board_vector4
                self.white_move_vector = new_potential_coords_vector4
            elif selection == 'five':
                self.white_board_vector = new_potential_white_board_vector5
                self.white_move_vector = new_potential_coords_vector5
            elif selection == 'six':
                self.white_board_vector = new_potential_white_board_vector6
                self.white_move_vector = new_potential_coords_vector6
            elif selection == 'seven':
                self.white_board_vector = new_potential_white_board_vector7
                self.white_move_vector = new_potential_coords_vector7
            elif selection == 'eight':
                self.white_board_vector = new_potential_white_board_vector8
                self.white_move_vector = new_potential_coords_vector8
    #    print('')
 #       print('white board vector', self.white_board_vector)
  #      print('white coords vector', self.white_move_vector)
     #   print('')
    def black_queen(self, i, j):
   #     print('BLACK QUEEN')
      #  print('')
        self.black_move_vector = []
        self.black_board_vector = []
        potential_black_board_vector1 = []
        potential_black_board_vector2 = []
        potential_black_board_vector3 = []
        potential_black_board_vector4 = []
        potential_black_board_vector5 = []
        potential_black_board_vector6 = []
        potential_black_board_vector7 = []
        potential_black_board_vector8 = []
        potential_coords_vector1 = []
        potential_coords_vector2 = []
        potential_coords_vector3 = []
        potential_coords_vector4 = []
        potential_coords_vector5 = []
        potential_coords_vector6 = []
        potential_coords_vector7 = []
        potential_coords_vector8 = []
        new_potential_black_board_vector1 = []
        new_potential_black_board_vector2 = []
        new_potential_black_board_vector3 = []
        new_potential_black_board_vector4 = []
        new_potential_black_board_vector5 = []
        new_potential_black_board_vector6 = []
        new_potential_black_board_vector7 = []
        new_potential_black_board_vector8 = []
        new_potential_coords_vector1 = []
        new_potential_coords_vector2 = []
        new_potential_coords_vector3 = []
        new_potential_coords_vector4 = []
        new_potential_coords_vector5 = []
        new_potential_coords_vector6 = []
        new_potential_coords_vector7 = []
        new_potential_coords_vector8 = []
        new_potential_black_board_vector_list = []
        self.piece_index = (self.i_black_index, self.j_black_index)
        """up"""
        index1 = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
        """down"""
        index2 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
        """left"""
        index3 = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]
        """right"""
        index4 = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
        """up_left"""
        index5 = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]
        """up_right"""
        index6 = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
        """down_left"""
        index7 = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
        """down_right"""
        index8 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
 #       print('selected piece index', i, j)
        """define adjusted index1"""
        for x in range(0, 7):
            index1[x][0] = index1[x][0] + i
            index1[x][1] = index1[x][1] + j
  #      print('new index1', index1)
        """define adjusted index2"""
        for x in range(0, 7):
            index2[x][0] = index2[x][0] + i
            index2[x][1] = index2[x][1] + j
   #     print('new index2', index2)
        """define adjusted index3"""
        for x in range(0, 7):
            index3[x][0] = index3[x][0] + i
            index3[x][1] = index3[x][1] + j
    #    print('new index3', index3)
        """define adjusted index4"""
        for x in range(0, 7):
            index4[x][0] = index4[x][0] + i
            index4[x][1] = index4[x][1] + j
     #   print('new index4', index4)
        for x in range(0, 7):
            index5[x][0] = index5[x][0] + i
            index5[x][1] = index5[x][1] + j
      #  print('new index1', index5)
        """define adjusted index2"""
        for x in range(0, 7):
            index6[x][0] = index6[x][0] + i
            index6[x][1] = index6[x][1] + j
       # print('new index6', index6)
        """define adjusted index3"""
        for x in range(0, 7):
            index7[x][0] = index7[x][0] + i
            index7[x][1] = index7[x][1] + j
#        print('new index7', index7)
        """define adjusted index4"""
        for x in range(0, 7):
            index8[x][0] = index8[x][0] + i
            index8[x][1] = index8[x][1] + j
 #       print('new index8', index8)
        """define index position to be removed"""
        remove1 = []
        """REMOVE up"""
        for i in range(0, len(index1)):
            if index1[i][0] < 0:
                remove1.append(i)
        for i in range(0, len(remove1)):
            index1.pop(remove1[i] - i)
        remove2 = []
        """REMOVE down"""
        for i in range(0, len(index2)):
            if index2[i][0] > 7:
                remove2.append(i)
        for i in range(0, len(remove2)):
            index2.pop(remove2[i] - i)
        remove3 = []
        """REMOVE left"""
        for i in range(0, len(index3)):
            if index3[i][1] < 0:
                remove3.append(i)
        for i in range(0, len(remove3)):
            index3.pop(remove3[i] - i)
        remove4 = []
        """REMOVE right"""
        for i in range(0, len(index4)):
            if index4[i][1] > 7:
                remove4.append(i)
        for i in range(0, len(remove4)):
            index4.pop(remove4[i] - i)
        remove5 = []
        """REMOVE up_left"""
        for i in range(0, len(index5)):
            if index5[i][1] < 0:
                remove5.append(i)
        for i in range(0, len(remove5)):
            index5.pop(remove5[i] - i)
        remove5 = []
        for i in range(0, len(index5)):
            if index5[i][0] < 0:
                remove5.append(i)
        for i in range(0, len(remove5)):
            index5.pop(remove5[i] - i)
        remove6 = []
        """REMOVE up_right"""
        for i in range(0, len(index6)):
            if index6[i][1] > 7:
                remove6.append(i)
        for i in range(0, len(remove6)):
            index6.pop(remove6[i] - i)
        remove6 = []
        for i in range(0, len(index6)):
            if index6[i][0] < 0:
                remove6.append(i)
        for i in range(0, len(remove6)):
            index6.pop(remove6[i] - i)
        remove7 = []
        """REMOVE down_left"""
        for i in range(0, len(index7)):
            if index7[i][0] > 7:
                remove7.append(i)
        for i in range(0, len(remove7)):
            index7.pop(remove7[i] - i)
        remove7 = []
        for i in range(0, len(index7)):
            if index7[i][1] < 0:
                remove7.append(i)
        for i in range(0, len(remove7)):
            index7.pop(remove7[i] - i)
        remove8 = []
        """REMOVE down_right"""
        for i in range(0, len(index8)):
            if index8[i][1] > 7:
                remove8.append(i)
        for i in range(0, len(remove8)):
            index8.pop(remove8[i] - i)
        remove8 = []
        for i in range(0, len(index8)):
            if index8[i][0] > 7:
                remove8.append(i)
        for i in range(0, len(remove8)):
            index8.pop(remove8[i] - i)
       # print('')
  #      print('final BLACK INDEX1 result', index1)
   #     print('final BLACK INDEX2 result', index2)
    #    print('final BLACK INDEX3 result', index3)
     #   print('final BLACK INDEX4 result', index4)
      #  print('final BLACK INDEX5 result', index5)
       # print('final BLACK INDEX6 result', index6)
 #       print('final BLACK INDEX7 result', index7)
  #      print('final BLACK INDEX8 result', index8)
        #print('')
        '''convert index's to board vectors'''
        """board/coords vector1"""
        for x in range(0, len(index1)):
            board_vector1 = self.mp[index1[x][0]][index1[x][1]]
            potential_black_board_vector1.append(board_vector1)
            coords_vector1 = self.bc[index1[x][0]][index1[x][1]]
            potential_coords_vector1.append(coords_vector1)
        """board/ coords vector2"""
        for x in range(0, len(index2)):
            board_vector2 = self.mp[index2[x][0]][index2[x][1]]
            potential_black_board_vector2.append(board_vector2)
            coords_vector2 = self.bc[index2[x][0]][index2[x][1]]
            potential_coords_vector2.append(coords_vector2)
        """board/coords vector3"""
        for x in range(0, len(index3)):
            board_vector3 = self.mp[index3[x][0]][index3[x][1]]
            potential_black_board_vector3.append(board_vector3)
            coords_vector3 = self.bc[index3[x][0]][index3[x][1]]
            potential_coords_vector3.append(coords_vector3)
        """board/coords vector4"""
        for x in range(0, len(index4)):
            board_vector4 = self.mp[index4[x][0]][index4[x][1]]
            potential_black_board_vector4.append(board_vector4)
            coords_vector4 = self.bc[index4[x][0]][index4[x][1]]
            potential_coords_vector4.append(coords_vector4)
        """board/ coords vector5"""
        for x in range(0, len(index5)):
            board_vector5 = self.mp[index5[x][0]][index5[x][1]]
            potential_black_board_vector5.append(board_vector5)
            coords_vector5 = self.bc[index5[x][0]][index5[x][1]]
            potential_coords_vector5.append(coords_vector5)
        """board/ coords vector6"""
        for x in range(0, len(index6)):
            board_vector6 = self.mp[index6[x][0]][index6[x][1]]
            potential_black_board_vector6.append(board_vector6)
            coords_vector6 = self.bc[index6[x][0]][index6[x][1]]
            potential_coords_vector6.append(coords_vector6)
        """board/coords vector7"""
        for x in range(0, len(index7)):
            board_vector7 = self.mp[index7[x][0]][index7[x][1]]
            potential_black_board_vector7.append(board_vector7)
            coords_vector7 = self.bc[index7[x][0]][index7[x][1]]
            potential_coords_vector7.append(coords_vector7)
        """board/coords vector8"""
        for x in range(0, len(index8)):
            board_vector8 = self.mp[index8[x][0]][index8[x][1]]
            potential_black_board_vector8.append(board_vector8)
            coords_vector8 = self.bc[index8[x][0]][index8[x][1]]
            potential_coords_vector8.append(coords_vector8)
        #print('')
   #     print('BLACK VECTOR1', potential_black_board_vector1)
    #    print('BLACK VECTOR2', potential_black_board_vector2)
     #   print('BLACK VECTOR3', potential_black_board_vector3)
      #  print('BLACK VECTOR4', potential_black_board_vector4)
       # print('BLACK VECTOR5', potential_black_board_vector5)
 #       print('BLACK VECTOR6', potential_black_board_vector6)
  #      print('BLACK VECTOR7', potential_black_board_vector7)
   #     print('BLACK VECTOR8', potential_black_board_vector8)
        #print('')
        for i in range(0, len(potential_black_board_vector1)):
            if potential_black_board_vector1[i] != '   ':
                piece = list(potential_black_board_vector1[i])
    #            print('PIECE1', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector1.append(potential_black_board_vector1[i])
                        new_potential_coords_vector1.append(potential_coords_vector1[i])
                break
            elif potential_black_board_vector1[i] == '   ':
                new_potential_black_board_vector1.append(potential_black_board_vector1[i])
                new_potential_coords_vector1.append(potential_coords_vector1[i])
        for i in range(0, len(potential_black_board_vector2)):
            if potential_black_board_vector2[i] != '   ':
                piece = list(potential_black_board_vector2[i])
     #           print('PIECE2', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector2.append(potential_black_board_vector2[i])
                        new_potential_coords_vector2.append(potential_coords_vector2[i])
                break
            elif potential_black_board_vector2[i] == '   ':
                new_potential_black_board_vector2.append(potential_black_board_vector2[i])
                new_potential_coords_vector2.append(potential_coords_vector2[i])
        for i in range(0, len(potential_black_board_vector3)):
            if potential_black_board_vector3[i] != '   ':
                piece = list(potential_black_board_vector3[i])
 #               print('PIECE3', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector3.append(potential_black_board_vector3[i])
                        new_potential_coords_vector3.append(potential_coords_vector3[i])
                break
            elif potential_black_board_vector3[i] == '   ':
                new_potential_black_board_vector3.append(potential_black_board_vector3[i])
                new_potential_coords_vector3.append(potential_coords_vector3[i])
        for i in range(0, len(potential_black_board_vector4)):
            if potential_black_board_vector4[i] != '   ':
                piece = list(potential_black_board_vector4[i])
  #              print('PIECE4', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector4.append(potential_black_board_vector4[i])
                        new_potential_coords_vector4.append(potential_coords_vector4[i])
                break
            elif potential_black_board_vector4[i] == '   ':
                new_potential_black_board_vector4.append(potential_black_board_vector4[i])
                new_potential_coords_vector4.append(potential_coords_vector4[i])
        for i in range(0, len(potential_black_board_vector5)):
            if potential_black_board_vector5[i] != '   ':
                piece = list(potential_black_board_vector5[i])
   #             print('PIECE5', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector5.append(potential_black_board_vector5[i])
                        new_potential_coords_vector5.append(potential_coords_vector5[i])
                break
            elif potential_black_board_vector5[i] == '   ':
                new_potential_black_board_vector5.append(potential_black_board_vector5[i])
                new_potential_coords_vector5.append(potential_coords_vector5[i])
        for i in range(0, len(potential_black_board_vector6)):
            if potential_black_board_vector6[i] != '   ':
                piece = list(potential_black_board_vector6[i])
    #            print('PIECE6', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector6.append(potential_black_board_vector6[i])
                        new_potential_coords_vector6.append(potential_coords_vector6[i])
                break
            elif potential_black_board_vector6[i] == '   ':
                new_potential_black_board_vector6.append(potential_black_board_vector6[i])
                new_potential_coords_vector6.append(potential_coords_vector6[i])
        for i in range(0, len(potential_black_board_vector7)):
            if potential_black_board_vector7[i] != '   ':
                piece = list(potential_black_board_vector7[i])
     #           print('PIECE7', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector7.append(potential_black_board_vector7[i])
                        new_potential_coords_vector7.append(potential_coords_vector7[i])
                break
            elif potential_black_board_vector7[i] == '   ':
                new_potential_black_board_vector7.append(potential_black_board_vector7[i])
                new_potential_coords_vector7.append(potential_coords_vector7[i])
        for i in range(0, len(potential_black_board_vector8)):
            if potential_black_board_vector8[i] != '   ':
                piece = list(potential_black_board_vector8[i])
#                print('PIECE8', piece)
                for n in range(0, len(piece)):
                    if piece[n] == 'w':
                        new_potential_black_board_vector8.append(potential_black_board_vector8[i])
                        new_potential_coords_vector8.append(potential_coords_vector8[i])
                break
            elif potential_black_board_vector8[i] == '   ':
                new_potential_black_board_vector8.append(potential_black_board_vector8[i])
                new_potential_coords_vector8.append(potential_coords_vector8[i])
 #       print('NEW BLACK VECTOR1', new_potential_black_board_vector1)
  #      print('NEW BLACK VECTOR2', new_potential_black_board_vector2)
   #     print('NEW BLACK VECTOR3', new_potential_black_board_vector3)
    #    print('NEW BLACK VECTOR4', new_potential_black_board_vector4)
     #   print('NEW BLACK VECTOR5', new_potential_black_board_vector5)
      #  print('NEW BLACK VECTOR6', new_potential_black_board_vector6)
       # print('NEW BLACK VECTOR7', new_potential_black_board_vector7)
 #       print('NEW BLACK VECTOR8', new_potential_black_board_vector8)
        #print('')
        if new_potential_black_board_vector1 != []:
            new_potential_black_board_vector_list.append('one')
        if new_potential_black_board_vector2 != []:
            new_potential_black_board_vector_list.append('two')
        if new_potential_black_board_vector3 != []:
            new_potential_black_board_vector_list.append('three')
        if new_potential_black_board_vector4 != []:
            new_potential_black_board_vector_list.append('four')
        if new_potential_black_board_vector5 != []:
            new_potential_black_board_vector_list.append('five')
        if new_potential_black_board_vector6 != []:
            new_potential_black_board_vector_list.append('six')
        if new_potential_black_board_vector7 != []:
            new_potential_black_board_vector_list.append('seven')
        if new_potential_black_board_vector8 != []:
            new_potential_black_board_vector_list.append('eight')
  #          print('index list', new_potential_black_board_vector_list)
        "select random index vector"
        if new_potential_black_board_vector_list != []:
            number_choice = np.random.randint(0, len(new_potential_black_board_vector_list))
            selection = new_potential_black_board_vector_list[number_choice]
            if selection == 'one':
                self.black_board_vector = new_potential_black_board_vector1
                self.black_move_vector = new_potential_coords_vector1
            elif selection == 'two':
                self.black_board_vector = new_potential_black_board_vector2
                self.black_move_vector = new_potential_coords_vector2
            elif selection == 'three':
                self.black_board_vector = new_potential_black_board_vector3
                self.black_move_vector = new_potential_coords_vector3
            elif selection == 'four':
                self.black_board_vector = new_potential_black_board_vector4
                self.black_move_vector = new_potential_coords_vector4
            elif selection == 'five':
                self.black_board_vector = new_potential_black_board_vector5
                self.black_move_vector = new_potential_coords_vector5
            elif selection == 'six':
                self.black_board_vector = new_potential_black_board_vector6
                self.black_move_vector = new_potential_coords_vector6
            elif selection == 'seven':
                self.black_board_vector = new_potential_black_board_vector7
                self.black_move_vector = new_potential_coords_vector7
            elif selection == 'eight':
                self.black_board_vector = new_potential_black_board_vector8
                self.black_move_vector = new_potential_coords_vector8
     #   print('')
   #     print('black board vector', self.black_board_vector)
    #    print('black coords vector', self.black_move_vector)
      #  print('')
    def white_pawn_promotion(self):
        print('COORDS',self.random_piece_board_coords)
        self.white.append(self.cycle)
        for m in range(0, 8):
            for n in range(0, 8):
                if self.bc[m][n] == self.random_piece_board_coords:
                    self.mp[m][n] == self.bc[m][n]
                    self.i_queen_index = m
                    self.j_queen_index = n
                    if self.mp[m][n] != '   ':
                        self.capture_black_piece()
                    break
        print('WHITE PIECE LIST', self.start_white_pieces)
        self.white_board_label()
        self.move_white_agent = []
        zero = -1000
        one = -1000
        self.move_white_agent.append(zero)
        self.move_white_agent.append(one)
        print('ARRAY', self.move_white_agent)
        self.frame.move(self.agent, self.move_white_agent[0], self.move_white_agent[1])
        self.move_white_agent = []
        if len(self.white) == 1:
            self.img_queen_w2 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w2.png')
            self.Qw2 = self.frame.create_image(self.bc[self.i_white_index-1][self.j_white_index], anchor=NW,
                                               image=self.img_queen_w2)
            self.frame.update()
        elif len(self.white) == 2:
            self.img_queen_w3 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w3.png')
            self.Qw3 = self.frame.create_image(self.bc[self.i_white_index-1][self.j_white_index], anchor=NW,
                                               image=self.img_queen_w3)
            self.frame.update()
        elif len(self.white) == 3:
            self.img_queen_w4 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w4.png')
            self.Qw4 = self.frame.create_image(self.bc[self.i_white_index-1][self.j_white_index], anchor=NW,
                                               image=self.img_queen_w4)
            self.frame.update()
        else:
            self.img_queen_w5 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_w5.png')
            self.Qw5 = self.frame.create_image(self.bc[self.i_white_index-1][self.j_white_index], anchor=NW,
                                               image=self.img_queen_w5)
            self.frame.update()
        print('CHOICE1', self.start_white_pieces[self.white_choice])
        for i in range(0, len(self.start_white_pieces)):
            if self.start_white_pieces[i] == self.start_white_pieces[self.white_choice]:
                if len(self.white) == 1:
                    print('CHOICE2', self.start_white_pieces[self.white_choice])
                    self.start_white_pieces.pop(i)
                    self.start_white_pieces.insert(i, 'Qw2')
                    break
                elif len(self.white) == 2:
                    print('CHOICE2', self.start_white_pieces[self.white_choice])
                    self.start_white_pieces.pop(i)
                    self.start_white_pieces.insert(i, 'Qw3')
                    break
                elif len(self.white) == 3:
                    print('CHOICE2', self.start_white_pieces[self.white_choice])
                    self.start_white_pieces.pop(i)
                    self.start_white_pieces.insert(i, 'Qw4')
                    break
                else:
                    print('CHOICE2', self.start_white_pieces[self.white_choice])
                    self.start_white_pieces.pop(i)
                    self.start_white_pieces.insert(i, 'Qw5')
                    break
        print('NEW  WHITE  LIST', self.start_white_pieces)
        print('')
        print(self.mp)
        print('Q index i', self.i_queen_index)
        print('Q index j', self.j_queen_index)
        if len(self.white) == 1:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qw2'
        elif len(self.white) == 2:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qw3'
        elif len(self.white) == 3:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qw4'
        else:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qw5'
        print(self.mp)
        print('')
        print('QUEEN PROMOTION')
        print('')
    def black_pawn_promotion(self):
        print('COORDS', self.random_piece_board_coords)
        self.black.append(self.cycle)
        for m in range(0, 8):
            for n in range(0, 8):
                if self.bc[m][n] == self.random_piece_board_coords:
                    self.mp[m][n] == self.bc[m][n]
                    self.i_queen_index = m
                    self.j_queen_index = n
                    if self.mp[m][n] != '   ':
                        self.capture_white_piece()
                    break
        print('BLACK PIECE LIST', self.start_black_pieces)
        self.black_board_label()
        self.move_black_agent = []
        zero = -1000
        one = -1000
        self.move_black_agent.append(zero)
        self.move_black_agent.append(one)
        print('ARRAY', self.move_black_agent)
        self.frame.move(self.agent, self.move_black_agent[0], self.move_black_agent[1])
        self.move_black_agent = []
        if len(self.black) == 1:
            self.img_queen_b2 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b2.png')
            self.Qb2 = self.frame.create_image(self.bc[self.i_black_index+1][self.j_black_index], anchor=NW,
                                               image=self.img_queen_b2)
            self.frame.update()
        elif len(self.black) == 2:
            self.img_queen_b3 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b3.png')
            self.Qb3 = self.frame.create_image(self.bc[self.i_black_index+1][self.j_black_index], anchor=NW,
                                               image=self.img_queen_b3)
            self.frame.update()
        elif len(self.black) == 3:
            self.img_queen_b4 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b4.png')
            self.Qb4 = self.frame.create_image(self.bc[self.i_black_index+1][self.j_black_index], anchor=NW,
                                               image=self.img_queen_b4)
            self.frame.update()
        else:
            self.img_queen_b5 = PhotoImage(file='C:/Users/user/PycharmProjects/CHESS/PIECES/queen_b5.png')
            self.Qb5 = self.frame.create_image(self.bc[self.i_black_index+1][self.j_black_index], anchor=NW,
                                               image=self.img_queen_b5)
            self.frame.update()
        print('CHOICE1', self.start_black_pieces[self.black_choice])
        for i in range(0, len(self.start_black_pieces)):
            if self.start_black_pieces[i] == self.start_black_pieces[self.black_choice]:
                if len(self.black) == 1:
                    print('CHOICE2', self.start_black_pieces[self.black_choice])
                    self.start_black_pieces.pop(i)
                    self.start_black_pieces.insert(i, 'Qb2')
                    break
                elif len(self.black) == 2:
                    print('CHOICE2', self.start_black_pieces[self.black_choice])
                    self.start_black_pieces.pop(i)
                    self.start_black_pieces.insert(i, 'Qb3')
                    break
                elif len(self.black) == 3:
                    print('CHOICE2', self.start_black_pieces[self.black_choice])
                    self.start_black_pieces.pop(i)
                    self.start_black_pieces.insert(i, 'Qb4')
                    break
                else:
                    print('CHOICE2', self.start_black_pieces[self.black_choice])
                    self.start_black_pieces.pop(i)
                    self.start_black_pieces.insert(i, 'Qb5')
                    break
        print('NEW  BLACK  LIST', self.start_black_pieces)
        print('')
        print('Q index i', self.i_queen_index)
        print('Q index j', self.j_queen_index)
        if len(self.black) == 1:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qb2'
        elif len(self.black) == 2:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qb3'
        elif len(self.black) == 3:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qb4'
        else:
            self.mp[self.i_queen_index][self.j_queen_index] = 'Qb5'
        print(self.mp)
        print('')
        print('QUEEN PROMOTION')
        print('')

    def white_candidates2(self):

            """define all possible legal 1st white moves """
            for x in range(0, len(self.start_white_pieces)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.mp[i][j] == self.start_white_pieces[x]:
                            self.selected_white_piece_coords = self.bc[i][j]
                            self.i_white_index = i
                            self.j_white_index = j
                            piece = list(self.start_white_pieces[x])
                            if piece[0] == 'P':
                                self.white_pawn(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'K' and piece[1] == 't':
                                self.white_knight(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'B':
                                self.white_bishop(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'R':
                                self.white_rook(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'Q':
                                self.white_queen(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif self.start_white_pieces == []:
                                break
            if self.cycle == 1:
                for i in range(0, len(self.start_white_pieces)):
                    if len(self.white_candidate_vector) < len(self.start_white_pieces):
                        self.white_candidate_vector.append('   ')
                self.white_candidate_vector.append(self.cycle)
            print('white candidate vector Z', self.white_candidate_vector)
            print('white board vector', self.white_candidate_board_vector)
            print('white move vector', self.white_candidate_move_vector)
            print('white index vector', self.white_candidate_index_vector)
            for i in range(0, len(self.white_candidate_vector)):
                if self.white_candidate_vector[i] == '   ':
                    self.len = i
                    break
            self.white_choice = np.random.randint(0, self.len)
            print('white choice', self.white_candidate_vector[self.white_choice])
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.mp[i][j] == self.white_candidate_vector[self.white_choice]:
                        self.selected_white_piece_coords = self.bc[i][j]
                        break
            print('selected white coords', self.selected_white_piece_coords)
            count = 0


    def white_candidates(self):

        #self.black_candidates()
        #hold = []
        #if self.cycle > 1:
         #   self.white_candidates2()
        self.len = ()
        if self.cycle == 1:
            """define all possible legal 1st white moves """
            for x in range(0, len(self.start_white_pieces)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.mp[i][j] == self.start_white_pieces[x]:
                            self.selected_white_piece_coords = self.bc[i][j]
                            self.i_white_index = i
                            self.j_white_index = j
                            piece = list(self.start_white_pieces[x])
                            if piece[0] == 'P':
                                self.white_pawn(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'K' and piece[1] == 't':
                                self.white_knight(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'B':
                                self.white_bishop(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'R':
                                self.white_rook(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'Q':
                                self.white_queen(i, j)
                                if self.white_board_vector != []:
                                    self.white_candidate_vector.append(self.start_white_pieces[x])
                                    self.white_candidate_board_vector.append(self.white_board_vector)
                                    self.white_candidate_move_vector.append(self.white_move_vector)
                                    self.white_candidate_index_vector.append(self.piece_index)
                            elif self.start_white_pieces == []:
                                break
            if self.cycle == 1:
                for i in range(0, len(self.start_white_pieces)):
                    if len(self.white_candidate_vector) < len(self.start_white_pieces):
                        self.white_candidate_vector.append('   ')
                self.white_candidate_vector.append(self.cycle)
            print('white candidate vector Z', self.white_candidate_vector)
            print('white board vector', self.white_candidate_board_vector)
            print('white move vector', self.white_candidate_move_vector)
            print('white index vector', self.white_candidate_index_vector)
            for i in range(0, len(self.white_candidate_vector)):
                if self.white_candidate_vector[i] == '   ':
                    self.len = i
                    break
            self.white_choice = np.random.randint(0, self.len)
            print('white choice', self.white_candidate_vector[self.white_choice])
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.mp[i][j] == self.white_candidate_vector[self.white_choice]:
                        self.selected_white_piece_coords = self.bc[i][j]
                        break
            print('selected white coords', self.selected_white_piece_coords)
            count = 0
    def black_candidates(self):
        hold = []
        #if self.cycle > 1:
         #   hold = self.black_candidate_vector
          #  if self.black_candidate_vector[15] == self.cycle -1:
           #     self.black_candidate_vector = hold
        #print('black vector',self.black_candidate_vector )
        if self.cycle == 1:
            for x in range(0, len(self.start_black_pieces)):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.mp[i][j] == self.start_black_pieces[x]:
                            self.selected_black_piece_coords = self.bc[i][j]
                            self.i_black_index = i
                            self.j_black_index = j
                            piece = list(self.start_black_pieces[x])
                            if piece[0] == 'P':
                                self.black_pawn(i, j)
                                if self.black_board_vector != []:
                                    self.black_candidate_vector.append(self.start_black_pieces[x])
                                    self.black_candidate_board_vector.append(self.black_board_vector)
                                    self.black_candidate_move_vector.append(self.black_move_vector)
                                    self.black_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'K' and piece[1] == 't':
                                self.black_knight(i, j)
                                if self.black_board_vector != []:
                                    self.black_candidate_vector.append(self.start_black_pieces[x])
                                    self.black_candidate_board_vector.append(self.black_board_vector)
                                    self.black_candidate_move_vector.append(self.black_move_vector)
                                    self.black_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'B':
                                self.black_bishop(i, j)
                                if self.black_board_vector != []:
                                    self.black_candidate_vector.append(self.start_black_pieces[x])
                                    self.black_candidate_board_vector.append(self.black_board_vector)
                                    self.black_candidate_move_vector.append(self.black_move_vector)
                                    self.black_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'R':
                                self.black_rook(i, j)
                                if self.black_board_vector != []:
                                    self.black_candidate_vector.append(self.start_black_pieces[x])
                                    self.black_candidate_board_vector.append(self.black_board_vector)
                                    self.black_candidate_move_vector.append(self.black_move_vector)
                                    self.black_candidate_index_vector.append(self.piece_index)
                            elif piece[0] == 'Q':
                                self.black_queen(i, j)
                                if self.black_board_vector != []:
                                    self.black_candidate_vector.append(self.start_black_pieces[x])
                                    self.black_candidate_board_vector.append(self.black_board_vector)
                                    self.black_candidate_move_vector.append(self.black_move_vector)
                                    self.black_candidate_index_vector.append(self.piece_index)
                            elif self.start_black_pieces == []:
                                break
            if self.cycle == 1:
                for i in range(0, len(self.start_black_pieces)):
                    if len(self.black_candidate_vector) < len(self.start_black_pieces):
                        self.black_candidate_vector.append('   ')
                self.black_candidate_vector.append(self.cycle)
            print('black candidate vector Z', self.black_candidate_vector)
            print('black board vector', self.black_candidate_board_vector)
            print('black move vector', self.black_candidate_move_vector)
            print('black index vector', self.black_candidate_index_vector)
            for i in range(0, len(self.black_candidate_vector)):
                if self.black_candidate_vector[i] == '   ':
                    self.len = i
                    break
            self.black_choice = np.random.randint(0, self.len)
            print('black choice', self.black_candidate_vector[self.black_choice])
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.mp[i][j] == self.black_candidate_vector[self.black_choice]:
                        self.selected_black_piece_coords = self.bc[i][j]
                        break
            print('selected black coords', self.selected_black_piece_coords)
            count = 0

    def white_board_label(self):
        if self.white_candidate_vector[self.white_choice] == 'Pw1':
            Pw1 = self.Pw1
            self.agent = Pw1
            #print('MOVE Pw1')
        elif self.white_candidate_vector[self.white_choice] == 'Pw2':
            Pw2 = self.Pw2
            self.agent = Pw2
            #print('MOVE Pw2')
        elif self.white_candidate_vector[self.white_choice] == 'Pw3':
            Pw3 = self.Pw3
            self.agent = Pw3
            #print('MOVE Pw3')
        elif self.white_candidate_vector[self.white_choice] == 'Pw4':
            Pw4 = self.Pw4
            self.agent = Pw4
            #print('MOVE Pw4')
        elif self.white_candidate_vector[self.white_choice] == 'Pw5':
            Pw5 = self.Pw5
            self.agent = Pw5
            #print('MOVE Pw5')
        elif self.white_candidate_vector[self.white_choice] == 'Pw6':
            Pw6 = self.Pw6
            self.agent = Pw6
            #print('MOVE Pw6')
        elif self.white_candidate_vector[self.white_choice] == 'Pw7':
            Pw7 = self.Pw7
            self.agent = Pw7
            #print('MOVE Pw7')
        elif self.white_candidate_vector[self.white_choice] == 'Pw8':
            Pw8 = self.Pw8
            self.agent = Pw8
            #print('MOVE Pw8')
        elif self.white_candidate_vector[self.white_choice] == 'Rw1':
            Rw1 = self.Rw1
            self.agent = Rw1
            #print('MOVE Rw1')
        elif self.white_candidate_vector[self.white_choice] == 'Bw1':
            Bw1 = self.Bw1
            self.agent = Bw1
            #print('MOVE Bw1')
        elif self.white_candidate_vector[self.white_choice] == 'Ktw1':
            Ktw1 = self.Ktw1
            self.agent = Ktw1
            #print('MOVE Ktw1')
        elif self.white_candidate_vector[self.white_choice] == 'Qw1':
            Qw1 = self.Qw1
            self.agent = Qw1
            #print('MOVE Qw1')
        elif self.white_candidate_vector[self.white_choice] == 'Qw2':
            Qw2 = self.Qw2
            self.agent = Qw2
            #print('MOVE Qw2')
        elif self.white_candidate_vector[self.white_choice] == 'Qw3':
            Qw3 = self.Qw3
            self.agent = Qw3
            #print('MOVE Qw3')
        elif self.white_candidate_vector[self.white_choice] == 'Qw4':
            Qw4 = self.Qw4
            self.agent = Qw4
            #print('MOVE Qw4')

        elif self.white_candidate_vector[self.white_choice] == 'Qw5':
            Qw5 = self.Qw5
            self.agent = Qw5
            #print('MOVE Qw5')
        elif self.white_candidate_vector[self.white_choice] == 'Kw':
            Kw = self.Kw
            self.agent = Kw
            #print('MOVE Kw')
        elif self.white_candidate_vector[self.white_choice] == 'Bw2':
            Bw2 = self.Bw2
            self.agent = Bw2
            #print('MOVE Bw2')
        elif self.white_candidate_vector[self.white_choice] == 'Ktw2':
            Ktw2 = self.Ktw2
            self.agent = Ktw2
            #print('MOVE Ktw2')
        elif self.white_candidate_vector[self.white_choice] == 'Rw2':
            Rw2 = self.Rw2
            self.agent = Rw2
            #print('MOVE Rw2')
    def black_board_label(self):
        #print('BBL')
        if self.black_candidate_vector[self.black_choice] == 'Pb1':
            Pb1 = self.Pb1
            self.agent = Pb1
         #   print('MOVE Pb1')
        elif self.black_candidate_vector[self.black_choice] == 'Pb2':
            Pb2 = self.Pb2
            self.agent = Pb2
          #  print('MOVE Pb2')
        elif self.black_candidate_vector[self.black_choice] == 'Pb3':
            Pb3 = self.Pb3
            self.agent = Pb3
           # print('MOVE Pb3')
        elif self.black_candidate_vector[self.black_choice] == 'Pb4':
            Pb4 = self.Pb4
            self.agent = Pb4
            #print('MOVE Pb4')
        elif self.black_candidate_vector[self.black_choice] == 'Pb5':
            Pb5 = self.Pb5
            self.agent = Pb5
    #        print('MOVE Pb5')
        elif self.black_candidate_vector[self.black_choice] == 'Pb6':
            Pb6 = self.Pb6
            self.agent = Pb6
     #       print('MOVE Pb6')
        elif self.black_candidate_vector[self.black_choice] == 'Pb7':
            Pb7 = self.Pb7
            self.agent = Pb7
      #      print('MOVE Pb7')
        elif self.black_candidate_vector[self.black_choice] == 'Pb8':
            Pb8 = self.Pb8
            self.agent = Pb8
       #     print('MOVE Pb8')
        elif self.black_candidate_vector[self.black_choice] == 'Rb1':
            Rb1 = self.Rb1
            self.agent = Rb1
        #    print('MOVE Rb1')
        elif self.black_candidate_vector[self.black_choice] == 'Ktb1':
            Ktb1 = self.Ktb1
            self.agent = Ktb1
         #   print('MOVE Ktb1')
        elif self.black_candidate_vector[self.black_choice] == 'Bb1':
            Bb1 = self.Bb1
            self.agent = Bb1
          #  print('MOVE Bb1')
        elif self.black_candidate_vector[self.black_choice] == 'Qb1':
            Qb1 = self.Qb1
            self.agent = Qb1
           # print('MOVE Qb1')
        elif self.black_candidate_vector[self.black_choice] == 'Qb2':
            Qb2 = self.Qb2
            self.agent = Qb2
            #print('MOVE Qb2')
        elif self.black_candidate_vector[self.black_choice] == 'Qb3':
            Qb3 = self.Qb3
            self.agent = Qb3
    #        print('MOVE Qb3')
        elif self.black_candidate_vector[self.black_choice] == 'Qb4':
            Qb4 = self.Qb4
            self.agent = Qb4
     #       print('MOVE Qb4')
        elif self.black_candidate_vector[self.black_choice] == 'Qb5':
            Qb5 = self.Qb5
            self.agent = Qb5
      #      print('MOVE Qb5')
        elif self.black_candidate_vector[self.black_choice] == 'Kb':
            Kb = self.Kb
            self.agent = Kb
       #     print('MOVE Kb')
        elif self.black_candidate_vector[self.black_choice] == 'Bb2':
            Bb2 = self.Bb2
            self.agent = Bb2
        #    print('MOVE Bb2')
        elif self.black_candidate_vector[self.black_choice] == 'Ktb2':
            Ktb2 = self.Ktb2
            self.agent = Ktb2
 #           print('MOVE Ktb2')
        elif self.black_candidate_vector[self.black_choice] == 'Rb2':
            Rb2 = self.Rb2
            self.agent = Rb2
  #          print('MOVE Rb2')

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
        elif self.white_board_vector[self.move] == 'Qb1':
            Qb1 = self.Qb1
            self.agent = Qb1
        elif self.white_board_vector[self.move] == 'Qb2':
            Qb2 = self.Qb2
            self.agent = Qb2
        elif self.white_board_vector[self.move] == 'Qb3':
            Qb3 = self.Qb3
            self.agent = Qb3
        elif self.white_board_vector[self.move] == 'Qb4':
            Qb4 = self.Qb4
            self.agent = Qb4
        elif self.white_board_vector[self.move] == 'Qb5':
            Qb5 = self.Qb5
            self.agent = Qb5
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
        elif self.black_board_vector[self.move] == 'Qw1':
            Qw1 = self.Qw1
            self.agent = Qw1
        elif self.black_board_vector[self.move] == 'Qw2':
            Qw2 = self.Qw2
            self.agent = Qw2
        elif self.black_board_vector[self.move] == 'Qw3':
            Qw3 = self.Qw3
            self.agent = Qw3
        elif self.black_board_vector[self.move] == 'Qw4':
            Qw4 = self.Qw4
            self.agent = Qw4
        elif self.black_board_vector[self.move] == 'Qw5':
            Qw5 = self.Qw5
            self.agent = Qw5
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
        print('MOVE INDEX number', self.move)
        print('Capture Black Piece vector', self.white_board_vector)
        print('Capture Black Piece move', self.white_board_vector[self.move])
        print('PIECE SELECTIONS', self.start_black_pieces)
        for i in range(0, len(self.start_black_pieces)):
            if self.start_black_pieces[i] == self.white_board_vector[self.move]:
                self.start_black_pieces.pop(i)
                self.start_black_pieces.insert(i, '   ')
                print('NEW  BLACK  LIST', self.start_black_pieces)
                print('REMOVE PIECE FROM BOARD')
                """REMOVE PIECE FROM BOARD"""
                break
        self.black_graphic_board_label()
        print('AGENT', self.agent)
        self.move_white_agent = []
        zero = -1000
        one = -1000
        self.move_white_agent.append(zero)
        self.move_white_agent.append(one)
        print('ARRAY', self.move_white_agent)
        self.frame.move(self.agent, self.move_white_agent[0], self.move_white_agent[1])
        self.move_white_agent = []

    def capture_white_piece(self):
        print('MOVE INDEX number', self.move)
        print('Capture White Piece vector', self.black_board_vector)
        print('Capture White Piece move', self.black_board_vector[self.move])
        print('PIECE SELECTIONS', self.start_white_pieces)
        for i in range(0, len(self.start_white_pieces)):
            if self.start_white_pieces[i] == self.black_board_vector[self.move]:
                self.start_white_pieces.pop(i)
                self.start_white_pieces.insert(i, '   ')
                print('NEW  WHITE  LIST', self.start_white_pieces)
                print('REMOVE PIECE FROM BOARD')
                """REMOVE PIECE FROM BOARD"""
                break
        self.white_graphic_board_label()
        print('AGENT', self.agent)
        self.move_black_agent = []
        zero = -1000
        one = -1000
        self.move_black_agent.append(zero)
        self.move_black_agent.append(one)
        print('ARRAY', self.move_black_agent)
        self.frame.move(self.agent, self.move_black_agent[0], self.move_black_agent[1])
        self.frame.update()
        self.move_black_agent = []

    def move_random_piece(self):
        self.pieces()
        self.board_data()
        self.board()
        self.cycle = 0
        piece = []
        for z in range(1, 2):
            print('NEXT MOVE')
            self.cycle = z
            flag = ()
            print('i =', z)
            self.white_candidates()
            '''change'''
            self.hold_index = self.white_candidate_index_vector[self.white_choice]
            print('INDEX',self.hold_index)
            self.white_board_label()
            """select random move"""
            self.white_candidate_move_vector = self.white_candidate_move_vector[self.white_choice]
            self.move = np.random.randint(0, len(self.white_candidate_move_vector))
            """MOVE piece"""
            self.random_piece_board_coords = self.white_candidate_move_vector[self.move]
            selection = self.random_piece_board_coords
            """define np move array"""
            zero = selection[0] - self.selected_white_piece_coords[0]
            one = selection[1] - self.selected_white_piece_coords[1]
            self.move_white_agent.append(zero)
            self.move_white_agent.append(one)
            """MOVE WHITE PIECE ON CHESS BOARD"""
            self.frame.move(self.agent, self.move_white_agent[0], self.move_white_agent[1])
            #time.sleep(0.01)
            self.frame.update()
            self.move_white_agent = []
            """REMOVE BLACK PIECE"""
            piece = list(self.white_board_vector_choice)
            for a in range(0, len(piece)):
                if piece[a] == 'b':
                    print('CAPTURE BLACK PIECE')
                    self.capture_black_piece()
                    print('BREAK')
                    break
            """update piece matrix"""
            for m in range(0, 8):
                for n in range(0, 8):
                    if self.bc[m][n] == self.random_piece_board_coords:
                        print('index', m, n)
                        self.mp[m][n] == self.bc[m][n]
                        hold = self.mp[m][n]
                        self.mp[m][n] = self.mp[self.hold_index[0]][self.hold_index[1]]
                        self.mp[self.hold_index[0]][self.hold_index[1]] = hold
                        if self.mp[self.hold_index[0]][self.hold_index[1]] != '   ':
                            self.mp[self.hold_index[0]][self.hold_index[1]] = '   '
                        print('choice number', self.white_choice)
                        print('index vector', self.white_candidate_index_vector)
                        self.white_candidate_index_vector.pop(self.white_choice)
                        self.white_candidate_index_vector.insert(self.white_choice, (m, n))
                        print('new index', self.white_candidate_index_vector)
                        print('')
            if self.i_white_index == 1:
                piece = list(self.white_candidate_vector[self.white_choice])
                print('WHITE PIECE', piece)
                print('')
                if piece[0] == 'P':
                    print('INDEX IS 1 PROMOTION CALL')
                    self.white_pawn_promotion()
                    print('WHITE WINS HAVING QUEENED A PAWN')
                    #break
            """MOVE BLACK PIECES"""
            self.black_candidates()
            self.hold_index = self.black_candidate_index_vector[self.black_choice]
            print('INDEX', self.hold_index)
            self.black_board_label()
            """select random move"""
            self.black_candidate_move_vector = self.black_candidate_move_vector[self.black_choice]
            self.move = np.random.randint(0, len(self.black_candidate_move_vector))
            """MOVE piece"""
            self.random_piece_board_coords = self.black_candidate_move_vector[self.move]
            selection = self.random_piece_board_coords
            """define np move array"""
            zero = selection[0] - self.selected_black_piece_coords[0]
            one = selection[1] - self.selected_black_piece_coords[1]
            self.move_black_agent.append(zero)
            self.move_black_agent.append(one)
            """MOVE BLACK PIECE ON CHESS BOARD"""
            self.frame.move(self.agent, self.move_black_agent[0], self.move_black_agent[1])
            #self.move_black_agent = []
            #time.sleep(0.01)
            self.frame.update()
            """REMOVE WHITE PIECE"""
            piece = list(self.black_candidate_board_vector[self.move])
            for i in range(0, len(piece)):
                if piece[i] == 'w':
                    print('CAPTURE WHITE PIECE')
                    self.capture_white_piece()
                    print('BREAK')
                    break
            """update piece matrix"""
            for m in range(0, 8):
                for n in range(0, 8):
                    if self.bc[m][n] == self.random_piece_board_coords:
                        print('index', m, n)
                        self.mp[m][n] == self.bc[m][n]
                        hold = self.mp[m][n]
                        self.mp[m][n] = self.mp[self.hold_index[0]][self.hold_index[1]]
                        self.mp[self.hold_index[0]][self.hold_index[1]] = hold
                        if self.mp[self.hold_index[0]][self.hold_index[1]] != '   ':
                            self.mp[self.hold_index[0]][self.hold_index[1]] = '   '
                        print(self.mp)
                        print('choice number', self.black_choice)
                        print('index vector', self.black_candidate_index_vector)
                        self.black_candidate_index_vector.pop(self.black_choice)
                        self.black_candidate_index_vector.insert(self.black_choice, (m, n))
                        print('new index', self.black_candidate_index_vector)
                        print('')
            if self.i_black_index == 6:
                piece = list(self.black_candidate_vector[self.black_choice])
                print('BLACK PIECE', piece)
                print('')
                if piece[0] == 'P':
                    print('INDEX IS 1 PROMOTION CALL')
                    self.black_pawn_promotion()
                    print('BLACK WINS HAVING QUEENED A PAWN')
                    #break


        self.root.mainloop()

data = ChessWorld()

#data.board()
# data.board_data()
#data.white_piece_vector()
# data.black_piece_vector()
#data.random_white_move()
data.move_random_piece()
# data.white_board_label()
# data.black_board_label()
#data.data_array()
