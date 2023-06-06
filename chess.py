class Chessboard:
    def __init__(self):
        self.board = [[True for _x in range(8) ] for _y in range(8)]
        self.notation_map = [{'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}, {'7': '1', '6': '2', '5': '3', '4': '2', '3': '5', '2': '6', '1': '7', '0': '0'}]

    def print_(self):
        for item in self.board:
            print(item)

    def check_if_occupied(self, coords) -> bool:
        x, y = coords
        if self.board[x][y] is True:
            return True
        else:
            return False

    def calculate_possible_moves(self, piece):
        pass

    def init_pieces(self):
            
        # ROOKS

        rook_black_start = [[0, 0], [0, 7]]
        rook_white_start = [[7, 7], [7, 0]]

        for item in rook_white_start:
            y, x = item
            self.board[y][x] = Rook(item, "white", self.notation_map) 

        for item in rook_black_start:
            y, x = item
            self.board[y][x] = Rook(item, "black", self.notation_map) 


class Rook:
    def __init__(self, position, color, notation_map):
        self.color = color
        self.position = position
        self.notation_map = notation_map

    def __repr__(self):
        y, x = self.position
        y = self.notation_map[1][str(y)]
        x = self.notation_map[0][str(x)]
        return f"{self.color} rook at {x} {y}"





chess = Chessboard()
chess.init_pieces()

chess.print_()