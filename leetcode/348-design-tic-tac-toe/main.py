class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.ht_row = n*[0]
        self.ht_col = n*[0]
        self.ht_diag1 = 0
        self.ht_diag2 = 0

    def move(self, row, col, player):
        """
        2nd approach: 
        1. save player1 as +1, save player2 as -1 for each rowcount, colcount, diagonal count, antidiagonal count
        2. when any entity reach N, the player wins the game

        Time    O(1)
        Space   O(n*n)
        44 ms, faster than 84.21%
        26feb2019
        """
        score = 0
        if player == 1:
            score = 1
        else:
            score = -1
        self.ht_row[row] += score
        self.ht_col[col] += score
        if row == col:
            self.ht_diag1 += score
        if row + col == self.n - 1:
            self.ht_diag2 += score

        ifWin = abs(self.ht_row[row]) == self.n\
            or abs(self.ht_col[col]) == self.n \
            or abs(self.ht_diag1) == self.n \
            or abs(self.ht_diag2) == self.n

        if ifWin:
            return player
        return 0
