import sys
from math import ceil

from util import asserter


# Observation:
# - I think “perfect play” means not putting the opposition in the position to win on their next turn.


def p1_wins(n) -> bool:
    """
    Run the match backwards, tracking the lowest checkmate state.

    Time: O(log n)
    Space: 1
    """
    winning_value = n
    losing_value = sys.maxsize
    curr_value = winning_value

    while curr_value > 9:
        if curr_value == winning_value:
            losing_value = ceil(winning_value / 9)
            curr_value = losing_value
        else:
            winning_value = ceil(losing_value / 2)
            curr_value = winning_value

    if curr_value > 2 and curr_value == losing_value:
        return True  # bad checkmate state for p1 can be avoided by picking a smaller starting number

    return curr_value == winning_value


asserter(lambda: p1_wins(162), True)
asserter(lambda: p1_wins(17), False)
asserter(lambda: p1_wins(34012226), True)
asserter(lambda: p1_wins(2), True)
asserter(lambda: p1_wins(19), True)
