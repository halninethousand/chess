from typing import List

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
        if self.board[y][x] is True:
            return False 
        else:
            return True

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

    def square_check(self, square, possible_squares, can_take):
        y, x = square
        if self.is_valid((y, x)):
            if not self.is_occupied((y, x)):
                possible_squares.append((y, x))
            else:
                can_take.append((y, x))
        return possible_squares, can_take 

    def rook_possibles(self, piece_at, possible_squares, can_take):
        y, x = piece_at

        # check down 
        for _ in range(8):
            y += 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)

        # check up
        y, _ = piece_at
        for _ in range(8):
            y -= 1 
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)

        #check right
        for _ in range(8):
            x += 1 
            possible_squares, can_take = self.square_check((y,x), possible_squares, can_take)

        # check left
        _, x = piece_at
        for _ in range(8):
            x -= 1 
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)
        return possible_squares, can_take

    def bishop_possibles(self, piece_at, possible_squares, can_take):
        y, x = piece_at

        # check down right
        for _ in range(8):
            x += 1
            y += 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)

        y, x = piece_at


        # check up left
        for _ in range(8):
            x -= 1
            y -= 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)

        y, x = piece_at

        # check up right 
        for _ in range(8):
            x += 1
            y -= 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)

        y, x = piece_at

        # check up left 
        for _ in range(8):
            x += 1
            y -= 1
            possible_squares, can_take = self.square_check((y, x), possible_squares, can_take)

        return possible_squares, can_take

    def move_logic(self, piece_at):
        y, x = piece_at
        possible_squares = list() 
        can_take = list()   

        if type(self.board[y][x]) == Rook:
           possible_squares, can_take = self.rook_possibles(piece_at, possible_squares, can_take)

        if type(self.board[y][x]) == Bishop:
            possible_squares, can_take = self.bishop_possibles(piece_at, possible_squares, can_take)

        moves = set()
        takes = set()

        for item in possible_squares:
            moves.add(self.coords_to_algebraic_map[item])
        print(self.board[y][x].__class__.__name__, "can move to ", moves)

        for item in can_take:
            takes.add(self.coords_to_algebraic_map[item])
        print(self.board[y][x].__class__.__name__, "can move to ", takes)

    def init_pieces(self):
            
        # Rooks

        rook_black_start = [[0, 0], [0, 7]]
        rook_white_start = [[7, 7], [7, 0]]

        for item in rook_white_start:
            y, x = item
            self.board[y][x] = Rook(item, "W") 

        for item in rook_black_start:
            y, x = item
            self.board[y][x] = Rook(item, "B") 

        # Bishops

        bishop_white_start = [[7, 2], [7, 5]]
        bishop_black_start = [[0, 2], [0, 5]]

        for item in bishop_white_start:
            y, x = item
            self.board[y][x] = Bishop(item, "W") 

        for item in bishop_black_start:
            y, x = item
            self.board[y][x] = Bishop(item, "B") 

        # King

        king_white_start = [[7, 4]]
        king_black_start = [[0, 4]]

        for item in king_white_start:
            y, x = item
            self.board[y][x] = King(item, "W")

        for item in king_black_start:
            y, x = item
            self.board[y][x] = King(item, "B")

        queen_white_start = [[7, 3]]
        queen_black_start = [[0, 3]]

        for item in queen_white_start:
            y, x = item
            self.board[y][x] = Queen(item, "W")

        for item in queen_black_start:
            y, x = item
            self.board[y][x] = Queen(item, "B")

        knights_white_start = [[7, 1], [7, 6]]
        knights_black_start = [[0, 1], [0, 6]]

        for item in knights_white_start:
            y, x = item
            self.board[y][x] = Knight(item, "W")

        for item in knights_black_start:
            y, x = item
            self.board[y][x] = Knight(item, "B")

class Piece:
    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.notation_map = [{'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}, {'7': '1', '6': '2', '5': '3', '4': '2', '3': '5', '2': '6', '1': '7', '0': '8'}]

    def __repr__(self) -> str:
        y, x = self.position
        y = self.notation_map[1][str(y)]
        x = self.notation_map[0][str(x)]
        return f"{self.color}{self.__class__.__name__}{x}{y}"

    def __str__(self) -> str:
        return self.__class__.__name__

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


print(chess.move_logic((7, 2)))