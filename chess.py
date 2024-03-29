from typing import List, Tuple

class Chessboard:

    def __init__(self):
        self.board = [[True for _x in range(8) ] for _y in range(8)]
        self.algebraic_to_coords_map = {}
        self.coords_to_algebraic_map = {}
        self.generate_conversion_maps()

    def print_(self):
        for item in self.board:
            print(item)

    def is_occupied(self, position) -> bool:
        y, x = position 
        if isinstance(self.board[y][x], Piece):
            return True 
        else:
            return False

    def generate_conversion_maps(self):
        files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        
        for file_index, file in enumerate(files):
            for rank_index, rank in enumerate(ranks):
                coords = (rank_index, file_index)
                notation = f"{file}{rank}"
                self.algebraic_to_coords_map[notation] = coords
                self.coords_to_algebraic_map[coords] = notation

    def algebraic_to_coords(self, notation):
        return self.algebraic_to_coords_map[notation]

    def coords_to_algebraic(self, coords):
        return self.coords_to_algebraic_map[coords]
    
    def is_valid(self, position) -> bool:
        y, x = position
        if 0 <= y <= 7 and 0 <= x <= 7:
            return True
        return False

    def square_check(self, square, possible_squares, can_take, piece_at):
        y, x = square
        if self.is_valid((y, x)):
            if not self.is_occupied((y, x)):
                possible_squares.append((y, x))
            else:
                # exclude same color pieces from being taken
                if self.board[piece_at[0]][piece_at[1]].color != self.board[y][x].color:
                    can_take.append((y, x))
        return possible_squares, can_take 

    def rook_possibles(self, piece_at, possible_squares, can_take):
        y, x = piece_at

        # check down 
        for _ in range(8):
            y += 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        # check up
        y, _ = piece_at
        for _ in range(8):
            y -= 1 
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        #check right
        for _ in range(8):
            x += 1 
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        # check left
        _, x = piece_at
        for _ in range(8):
            x -= 1 
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)
        return possible_squares, can_take

    def bishop_possibles(self, piece_at, possible_squares, can_take):
        y, x = piece_at

        # check down right
        for _ in range(8):
            x += 1
            y += 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        y, x = piece_at

        # check down left
        for _ in range(8):
            x -= 1
            y += 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        y, x = piece_at

        # check up right 
        for _ in range(8):
            x += 1
            y -= 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        y, x = piece_at

        # check up left 
        for _ in range(8):
            x -= 1
            y -= 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        return possible_squares, can_take
    
    def king_possibles(self, piece_at, possible_squares, can_take):
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

        for item in directions:
            y, x = piece_at
            y += item[0]
            x += item[1]
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)
        return possible_squares, can_take

    def knight_possibles(self, piece_at, possible_squares, can_take):
        directions = ((-1, -2), (-2, -1), (-2, 1), (-1, -2), (1, 2), (2, 1), (1, -2), (-2, -1))

        for item in directions:
            y, x = piece_at
            y += item[0]
            x += item[1]
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take, piece_at)

        return possible_squares, can_take

    def queen_possibles(self, piece_at, possible_squares, can_take):
        possible_squares, can_take = self.rook_possibles(piece_at, possible_squares, can_take)
        possible_squares, can_take = self.bishop_possibles(piece_at, possible_squares, can_take)

        return possible_squares, can_take

    def move_logic(self, piece_at):
        y, x = piece_at
        possible_squares = list() 
        can_take = list()   

        if type(self.board[y][x]) == Rook:
           possible_squares, can_take = self.rook_possibles(piece_at, possible_squares, can_take)

        if type(self.board[y][x]) == Bishop:
           possible_squares, can_take = self.bishop_possibles(piece_at, possible_squares, can_take)

        if type(self.board[y][x]) == King:
            possible_squares, can_take = self.king_possibles(piece_at, possible_squares, can_take)

        if type(self.board[y][x]) == Knight:
            possible_squares, can_take = self.knight_possibles(piece_at, possible_squares, can_take)

        if type(self.board[y][x]) == Queen:
            possible_squares, can_take = self.queen_possibles(piece_at, possible_squares, can_take)
        


        moves = set()
        takes = set()

        for item in possible_squares:
            moves.add(self.coords_to_algebraic_map[item])
        print(self.board[y][x].__class__.__name__, "can move to", moves)

        for item in can_take:
            takes.add(self.coords_to_algebraic_map[item])
        print(self.board[y][x].__class__.__name__, "can take", takes)

        return moves, takes
    def init_pieces(self):
            
        # hard-coded starting position for every piece

        rook_black_start = ((0, 0), (0, 7))
        rook_white_start = ((7, 7), (7, 0))

        for item in rook_white_start:
            y, x = item
            self.board[y][x] = Rook(item, "W", self.coords_to_algebraic_map) 

        for item in rook_black_start:
            y, x = item
            self.board[y][x] = Rook(item, "B", self.coords_to_algebraic_map) 

        bishop_white_start = ((7, 2), (7, 5))
        bishop_black_start = ((0, 2), (0, 5))

        for item in bishop_white_start:
            y, x = item
            self.board[y][x] = Bishop(item, "W", self.coords_to_algebraic_map) 

        for item in bishop_black_start:
            y, x = item
            self.board[y][x] = Bishop(item, "B", self.coords_to_algebraic_map) 

        king_white_start = (7, 4)
        king_black_start = (0, 4)

        y, x = king_white_start
        self.board[y][x] = King(item, "W", self.coords_to_algebraic_map)

        y, x = king_black_start
        self.board[y][x] = King(item, "B", self.coords_to_algebraic_map)

        queen_white_start = (7, 3)
        queen_black_start = (0, 3)

        y, x = queen_white_start
        self.board[y][x] = Queen(item, "W", self.coords_to_algebraic_map)

        y, x = queen_black_start
        self.board[y][x] = Queen(item, "B", self.coords_to_algebraic_map)


        knights_white_start = ((7, 1), (7, 6))
        knights_black_start = ((0, 1), (0, 6))

        for item in knights_white_start:
            y, x = item
            self.board[y][x] = Knight(item, "W", self.coords_to_algebraic_map)

        for item in knights_black_start:
            y, x = item
            self.board[y][x] = Knight(item, "B", self.coords_to_algebraic_map)

class Piece:
    def __init__(self, position, color, coords_to_notation):
        self.color = color
        self._position = position
        self.coords_to_notation_map = coords_to_notation 

    def __repr__(self) -> str:
        return f"{self.color}{self.__class__.__name__}{self.coords_to_notation_map[tuple(self.position)]}"

    def __str__(self) -> str:
        return self.__class__.__name__

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        y, x = position
        if 0 <= y <= 7 and 0 <= x <= 7:
            self._position = position


class Rook(Piece):
    pass

class Bishop(Piece):
    pass

class King(Piece):
    pass

class Queen(Piece):
    pass

class Knight(Piece):
    pass

class Pawn(Piece):
    pass


chess = Chessboard()
chess.init_pieces()
chess.print_()


print(chess.move_logic((7, 3)))