"""
Brainstorming
- move everyone's money to one student, (money exchanged = slightly less than all), then distribute it evenly
  (money exchanged = slightly less than all). Total exchanged = slightly less than all * 2, so incorrect
- Sort by descending, pair every overexpensed student to an underexpensed student on the opposite end of the
  spectrum. Exchange money from overexp to underexp until overexp hits the avg. If money still needed for
  underexp student, use next overexp student.
- The observation is that you don't want to be exchanging money in such a way that a student ends up with
  temporarily more money only to need to get rid of that money again. So never give money to an overexp,
  and never give money to an underexp that would take them beyond the avg, and never take money from an
  overexp that would take them below the avg. This ensures that every exchange is optimally efficient.
- Can't we just calculate the cumulative money above the average that each above-average student used,
  and return that, without calculating the actual connections between the students for the txns? I
  assume so.
"""


def totalexchange(trips: list[list[float]]) -> list[float]:
    """
    :param trips: List of trips, where each trip is a list of expenses for each student.
    :return: Minimum money that needs to be moved from one student to another to equalize costs
             to the nearest cent.

    - Sum expenses, then divide to find average expense per student
    - For each above avg expensing student, accumulate a running sum
    - Return that running sum, which should be the minimal amount of money moved

    O(nm) time (n :: trips, m :: students expenses),
    O(1) space (factoring out return value)
    """
    money_to_move = []
    for expenses in trips:
        n = len(expenses)
        if n == 0:
            money_to_move.append(0)
        else:
            s = sum(student_exp for student_exp in expenses)
            avg = round(s / n, 2)

            min_money_exchanged = sum(student_exp - avg for student_exp in expenses if student_exp > avg)
            money_to_move.append(min_money_exchanged)

    return money_to_move
