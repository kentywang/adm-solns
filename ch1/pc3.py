from collections import Counter
from functools import reduce
from math import inf


# Writing this algorithm turned out to be easier/cleaner than expected!
def ausvote(cands: tuple[str, ...], ballots: list[tuple[int, ...]]) -> set[str]:
    """
    - Check 1st preference on each ballot, counting to see if any candidate gets >50% of the vote
    - If not, replace all lowest-counted candidates' spots on each ballot with the next preference,
      and recount
    - Repeat if necessary

    O(bc) time (b :: ballots, c :: candidates), O(b + c) space
    """

    def round_losers(acc, cur):
        lowest_cands, lc_votes = acc
        cand, cand_votes = cur

        if cand_votes < lc_votes:
            return [cand], cand_votes
        if cand_votes == lc_votes:
            lowest_cands.append(cand)
        return acc

    def candidate(vote: int):
        return cands[vote - 1]

    cand_ct = len(cands)
    ballotiters = [iter(b) for b in ballots]
    eliminated = []

    while len(eliminated) != cand_ct:
        c = Counter()  # new Counter after each elimination. Can be an array of O(c) space

        for ballotiter in ballotiters:
            while (top_pref := next(ballotiter, None)) in eliminated:
                pass
            if top_pref:
                c.update([top_pref])

        # Return most voted candidate if majority
        mostcommonvote, mcv_ct = c.most_common(1)[0]
        if mcv_ct > (c.total() / 2):
            return {candidate(mostcommonvote)}

        # Otherwise, eliminate lowest-ranking candidate(s)
        lowests, _ = reduce(round_losers, c.most_common(), ([], inf))

        eliminated += lowests

    return {candidate(e) for e in eliminated}
