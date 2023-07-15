from util import asserter

Coord = tuple[int, int]


# Each slot has 3 possible values
# there are n^2 slots
# (3)^4 = 81 possible game states if n = 2
# (3)^9 = 19K possible game states if n = 3
# (3)^16 = 43M possible game states if n = 4

# think of chmod numbering system
# if we represent each row by a character, then as n grows, the gamestate length grows at the same rate (n), rather than by n^2.
# so each row has 3^n states.
# if n = 2, then each row has 3^2 = 9 possible states
# if n = 3, then each row has 3^3 = 27 possible states
# if n = 4, then each row has 3^4 = 81 possible states
# but this is unsustainable. We have only a limited character set.

# we need sth more like this
# n = 3 => store 3/6/9 elements
# n = 4 => store 4/8/12 elements
# n = 5 => store 5/10/15 elements

# there are only 2 (diag) + 2n (n rows and n columns) lines that could win. Maybe we just need
# O(2 + 2n) space?
# each line
#

# 2   1
# 1    1
# 0   1 1
#
#     012
# 000100010101000
# becomes diag0 = 100, diag1 = 111, r0 = 100, r1 = 010, r2 = 101, c0 = 101, c1 = 010, c2 = 001
# checking each of these lines takes constant time, but checking all lines takes O(2+2n) time, so not the required O(1)

# could we have a string of n length represent the state somehow? but that would take n time to check if last move won,
# since the string must be parse characterwise.

# notice that for evaluating the last move, you just need to know what n is to know which of the lines to check. e.g.
# if move to check is (x, x), it's on a diag, so you only need to check one of the diags and a row and column.

# seems you always need to check a row, a column, and either 1 diag (if n is even, or checked coord isn't in center
# when n is odd) or 2 diag (only when checked coord is in center, which only happens when n is odd). thus you only
# need to check 3-4 values, so O(1) time. But we need to make sure each value check is constant, so not linear with n.
# So each value can't be a string. It could be a bit array but that would violate O(1) time if the bit arithmetic needed
# depended on the length of the array.

# ..figured it out. for each row/col/diag, store count of hits. when count is n for any of the 3-4 lines to check,
# that's when the move wins the game.


# 2   XOO
# 1   OXO
# 0   X X
#
#     012

class TicTacToe:
    """
    Assume O goes first.
    """

    def __init__(self, size):
        self.state = {
            'X': {
                'rows': [0] * size,
                'cols': [0] * size,
                'diags': [0, 0]  # bot left to top right 1st, top left to bot right 2nd
            },
            'O': {
                'rows': [0] * size,
                'cols': [0] * size,
                'diags': [0, 0]
            }
        }
        self.size = size
        self.turn = 0
        self.lastMove = None

    def push(self, *coords: Coord) -> bool:
        """
        Needs to be O(n) space (i.e wrt to the game board's length/width)
        """
        for c in coords:
            self._updateState(c)
            if self._checkWinner():
                return True

        # self.state = []
        return False

    def _updateState(self, c: Coord) -> None:
        """
        Needs to be O(1) time

        Brute-force: Just make concat each new coord into a list, which would be O(1) time. But this would not allow
        for constant time to check the winner.
        """
        x, y = c

        player = self.state['X'] if self.turn % 2 else self.state['O']

        player['rows'][x] += 1
        player['cols'][y] += 1
        if x == y:
            player['diags'][0] += 1
        if x + y + 1 == self.size:
            player['diags'][1] += 1

        self.lastMove = c
        self.turn += 1

    def _checkWinner(self) -> bool:
        """
        Needs to be O(1) time
        """
        last_turn = self.turn - 1
        x, y = self.lastMove
        player = self.state['X'] if last_turn % 2 else self.state['O']

        row_won = player['rows'][x] == self.size
        col_won = player['rows'][x] == self.size

        diag1_won = False
        diag2_won = False
        if x == y:
            diag1_won = player['diags'][0] == self.size
        if x + y + 1 == self.size:
            diag2_won = player['diags'][1] == self.size

        return any([row_won, col_won, diag1_won, diag2_won])


moves: list[Coord] = [
    (0, 1),  # O
    (1, 1),  # X
    (2, 1),  # O
    (0, 0),  # X
    (1, 2),  # O
    (0, 2),  # X
    (2, 2),  # O
    (2, 0),  # X wins
]
ttt = TicTacToe(3)
asserter(lambda: ttt.push(moves[0], moves[1]), False)
asserter(lambda: ttt.push(*moves[2:4]), False)
asserter(lambda: ttt.push(*moves[4:7]), False)
asserter(lambda: ttt.push(moves[7]), True)
