from ch1.pc3 import ausvote
from util import asserter

# Example case
asserter(lambda: ausvote(cands=('A', 'B', 'C'), ballots=[
    (1, 2, 3),
    (2, 1, 3),
    (2, 3, 1),
    (1, 2, 3),
    (3, 1, 2)]),
         {'A'})

# Tests eliminated candidates skipped until non-eliminated candidate reached
asserter(lambda: ausvote(cands=('A', 'B', 'C', 'D'), ballots=[
    (1, 2, 4, 3),
    (1, 2, 4, 3),
    (2, 1, 4, 3),
    (2, 3, 1, 4)]),
         {'D'})

# Tie case
asserter(lambda: ausvote(cands=('A', 'B'), ballots=[
    (1, 2),
    (2, 1)]),
         {'A', 'B'})

# Tie case 2
asserter(lambda: ausvote(cands=('A', 'B', 'C'), ballots=[
    (1, 2, 3),
    (2, 1, 3),
    (3, 1, 2)]),
         {'C', 'A', 'B'})
