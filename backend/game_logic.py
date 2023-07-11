class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Board:
    def __init__(self):
        self.board = self.create_board()

    @staticmethod
    def create_board():
        board = [['' for _ in range(9)] for _ in range(10)]
        pieces = ['Chariot', 'Horse', 'Elephant', 'Advisor', 'King', 'Advisor', 'Elephant', 'Horse', 'Chariot']
        colors = ['Red', 'Black']
        for i in range(2):
            for j in range(9):
                board[i*9][j] = Piece(pieces[j], colors[i])
                board[i*9+1][j] = Piece('Soldier', colors[i]) if j % 2 == 0 else ''
        return board

