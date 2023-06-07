class Chessboard:
    def __init__(self):
        self.board = [[True for _x in range(8) ] for _y in range(8)]
        self.notation_map = [{'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}, {'7': '1', '6': '2', '5': '3', '4': '2', '3': '5', '2': '6', '1': '7', '0': '8'}]

    def print_(self):
        for item in self.board:
            print(item)

    def check_if_occupied(self, coords) -> bool:
        x, y = coords
        if self.board[x][y] is True:
            return True
        else:
            return False

    def is_valid(self, position):
        y, x = position
        if 0 <= y <= 7 and 0 <= x <= 7:
            return True
        return False

    def calculate_possible_moves(self, position):
        y, x = position
        possible_squares = []
        # ROOK        
        if type(self.board[y][x]) == Rook:
            pass    

    def init_pieces(self):
            
        # ROOKS

        rook_black_start = [[0, 0], [0, 7]]
        rook_white_start = [[7, 7], [7, 0]]

        for item in rook_white_start:
            y, x = item
            self.board[y][x] = Rook(item, "W") 

        for item in rook_black_start:
            y, x = item
            self.board[y][x] = Rook(item, "B") 

        # BISHOPS

        bishop_white_start = [[7, 2], [7, 5]]
        bishop_black_start = [[0, 2], [0, 5]]

        for item in bishop_white_start:
            y, x = item
            self.board[y][x] = Bishop(item, "W") 

        for item in bishop_black_start:
            y, x = item
            self.board[y][x] = Bishop(item, "B") 

class Piece:
    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.notation_map = [{'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}, {'7': '1', '6': '2', '5': '3', '4': '2', '3': '5', '2': '6', '1': '7', '0': '8'}]

class Rook(Piece):
    # def __init__(self, position, color):
    #     # super().__init__(position, color)

    def __repr__(self):
        y, x = self.position
        y = self.notation_map[1][str(y)]
        x = self.notation_map[0][str(x)]
        return f"{self.color}rook{x}{y}"


class Bishop(Piece):
    # def __init__(self, position, color):
    #     super().__init__(position, color)

    def __repr__(self):
        y, x = self.position
        y = self.notation_map[1][str(y)]
        x = self.notation_map[0][str(x)]
        return f"{self.color}bishop{x}{y}"


chess = Chessboard()
chess.init_pieces()
chess.print_()