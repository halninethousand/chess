from typing import List

class Chessboard:
    def __init__(self):
        self.board = [[True for _x in range(8) ] for _y in range(8)]
        self.notation_map = [{'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}, {'7': '1', '6': '2', '5': '3', '4': '2', '3': '5', '2': '6', '1': '7', '0': '8'}]

    def print_(self):
        for item in self.board:
            print(item)

    def is_occupied(self, position) -> bool:
        y, x = position 
        if self.board[y][x] is True:
            return False 
        else:
            return True

    def correct_notation(self, coords) -> List:
        return [(self.notation_map[0][str(item[0])], self.notation_map[1][str(item[1])]) for item in coords]

    def is_valid(self, position) -> bool:
        y, x = position
        if 0 <= y <= 7 and 0 <= x <= 7:
            return True
        return False

    def square_check(self, square, possible_squares, can_take):
        y, x = square
        if self.is_valid((y, x)):
            pass
        else:
            return possible_squares, can_take 
        if not self.is_occupied((y, x)):
            possible_squares.append((y, x))
        elif self.is_occupied((y, x)):
            can_take.append((y, x))
            return possible_squares, can_take 

        return possible_squares, can_take 

    def action_loop(self, piece_at):
        y, x = piece_at
        possible_squares = []
        can_take = []
        iter_y = y
        iter_x = x

        if type(self.board[y][x]) == Rook:
            # check down 
            for _ in range(8):
                iter_y += 1
                possible_squares, can_take = self.square_check((iter_y, x), possible_squares, can_take)

            # check up
            iter_y = y # iter y hast to be brought back to original piece position
            for _ in range(8):
                iter_y -= 1 
                possible_squares, can_take = self.square_check((iter_y, x), possible_squares, can_take)

            #check right
            for _ in range(8):
                iter_x += 1 
                possible_squares, can_take = self.square_check((y, iter_x), possible_squares, can_take)

            # check left
            iter_x = x  # iter_x has to be brought back to original piece position 
            for _ in range(8):
                iter_x -= 1 
                possible_squares, can_take = self.square_check((y, iter_x), possible_squares, can_take)
            if possible_squares:
                return possible_squares
            else:
                return []
            
        if type(self.board[y][x]) == Bishop:
            # check down right
            for _ in range(8):
                iter_x += 1
                iter_y += 1
                possible_squares, can_take = self.square_check((iter_y, iter_x), possible_squares, can_take)

            iter_y, iter_x = y, x # go back to original values

            # check up left
            for _ in range(8):
                iter_x -= 1
                iter_y -= 1
                possible_squares, can_take = self.square_check((iter_y, iter_x), possible_squares, can_take)

            iter_y, iter_x = y, x # go back to original values

            # check up right 
            for _ in range(8):
                iter_x += 1
                iter_y -= 1
                possible_squares, can_take = self.square_check((iter_y, iter_x), possible_squares, can_take)

            iter_y, iter_x = y, x # go back to original values

            # check up left 
            for _ in range(8):
                iter_x += 1
                iter_y -= 1
                possible_squares, can_take = self.square_check((iter_y, iter_x), possible_squares, can_take)
        
        print(self.board[y][x].__class__.__name__, "can move to \n")
        print(self.correct_notation(possible_squares))

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

        for item in knights_white_start  :
            y, x = item
            self.board[y][x] = Knight(item, "W")

        for item in knights_black_start :
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



chess = Chessboard()
chess.init_pieces()
chess.print_()


print(chess.action_loop((7, 2)))