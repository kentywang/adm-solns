# Started 8/27
# Finished ___

from collections import deque
from functools import reduce
from itertools import combinations
from math import sqrt, inf
from random import randint
from profiler import profile


# from memory_profiler import profile


def calc_dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


@profile
def nearest_neighbor(g):
    unvisiteds = [True] * len(g)

    def get_unvisiteds():
        return [j for j, b in enumerate(unvisiteds) if b]

    order = []

    def closest_idx_dist(idxs, curr_idx):
        curr_min_dist = inf
        curr_closest_i = None

        for idx in idxs:
            if (dis := calc_dist(g[curr_idx], g[idx])) < curr_min_dist:
                curr_min_dist = dis
                curr_closest_i = idx

        return curr_closest_i, curr_min_dist

    # Visit first element of list
    curr_i = 0
    unvisiteds[curr_i] = False
    order.append(curr_i)
    total_dist = 0

    while unv_idxs := get_unvisiteds():
        i, d = closest_idx_dist(unv_idxs, curr_i)
        curr_i = i
        unvisiteds[curr_i] = False
        order.append(curr_i)
        total_dist += d

    total_dist += calc_dist(g[0], g[curr_i])

    return order, total_dist


@profile
def closest_pair(g):
    def pair_pts_from_distinct(vcs):
        """Returns all the valid pair combinations between vertices on the ends of the passed vertex chains"""
        # sets of combinable endpts, where each endpt is from a distinct chain
        endpts_w_chain_no = reduce(
            set.union,
            ({(chain[0], chain_no), (chain[-1], chain_no)} for chain_no, (chain, _) in enumerate(vcs))  # self deduping
        )  # looks like {(1, 0), (2, 0), (3, 1), (4, 1)}

        # skip combinations where two endpts from same chain are paired, then remove the chain numbers
        # also map it to a dict for readability
        return (
            list(  # no need to risk unexpected generator behavior if we need to traverse every element anyways
                map(
                    lambda pr_chn: {"pair": (pr_chn[0][0], pr_chn[1][0]),
                                    "chain_indices": (pr_chn[0][1], pr_chn[1][1])},
                    filter(
                        lambda pr: pr[0][1] != pr[1][1],
                        combinations(endpts_w_chain_no, 2)
                    )
                )
            )
        )

    def chains_with_shortest_dist(pr_chns):
        """
        Of the list of linkings betweens chains and their link distance,
        returns the indices of the two chains that have the shortest link distance between them
        """
        curr = {
            "chain_i": None,
            "chain_j": None,
            "dist": inf
        }

        dists = (calc_dist(g[pc["pair"][0]], g[pc["pair"][1]]) for pc in pr_chns)
        for pc, d in zip(pr_chns, dists):
            if d < curr["dist"]:
                curr = {
                    "pair": pc["pair"],
                    "chain_i": pc["chain_indices"][0],
                    "chain_j": pc["chain_indices"][1],
                    "dist": d
                }

        return curr

    def merge_chains(vcs, pair, chain_i, chain_j, dist):
        """Mutates the list argument provided."""
        vc1, vc2 = vertex_chains[chain_i], vertex_chains[chain_j]

        # filter out the two chains that will be merged, then add in the merged chain
        rest = [vc for chain_no, vc in enumerate(vcs) if chain_no != chain_i and chain_no != chain_j]

        # make sure orientation for merging is correct, important for final distance calculation
        vc1a = vc1[0][0]
        vc2a = vc2[0][0]

        if vc1a == pair[0]:
            vc1[0].reverse()
        if vc2a != pair[1]:
            vc2[0].reverse()

        merged = (vc1[0] + vc2[0], vc1[1] + vc2[1] + dist)

        vcs[:] = rest + [merged]

    vertex_chains = [(deque([i]), 0) for i, _ in enumerate(g)]  # list of tuple of vertices and total dist

    while len(vertex_chains) > 1:
        pairs_w_chain_no = pair_pts_from_distinct(vertex_chains)
        chain_nos_w_dist = chains_with_shortest_dist(pairs_w_chain_no)
        merge_chains(vertex_chains, **chain_nos_w_dist)

    # Finally, connect the chain together to form a tour
    vc_deq, total_dist = vertex_chains[0]
    endpt1, endpt2 = vc_deq[0], vc_deq[-1]
    total_dist += calc_dist(g[endpt1], g[endpt2])

    return vc_deq, total_dist


def func_test():
    graph1 = [(0, 0), (0, 1), (0, -2), (0, 5), (0, -10), (0, 21)]  # shortest is 31 * 2 = 62
    graph2 = [(-3, 0), (-3, 1), (0, 0), (0, 1), (3, 0), (3, 1)]  # shortest is 6 + 6 + 1 + 1 = 14

    print(nearest_neighbor(graph1))  # expect 1 + 3 + 7 + 15 + 31 + 21 = 78
    print(nearest_neighbor(graph2))  # expect 9 + sqrt(37) = 15.1

    print(closest_pair(graph1))  # expect 62
    print(closest_pair(graph2))  # expect 15.1


def perf_test():
    def test_tour_heuristics(n):
        print(f'\033[0;31mn: {n}\033[0m')
        graph = [(randint(-n, n), randint(-n, n)) for _ in range(0, n)]
        print(nearest_neighbor(graph)[1])
        print(closest_pair(graph)[1])

    test_tour_heuristics(100)
    test_tour_heuristics(200)
    test_tour_heuristics(400)


# func_test()
perf_test()

# Results
# n: 100
# nearest_neighbor: 4 KiB, 3 ms
# 2023.768245164767
# closest_pair: 4272 KiB, 356 ms
# 2039.4096178628715
# n: 200
# nearest_neighbor: 4 KiB, 15 ms
# 5663.23900541345
# closest_pair: 11704 KiB, 2821 ms
# 4814.492834218646
# n: 400
# nearest_neighbor: 0 KiB, 65 ms
# 15298.839718985993
# closest_pair: 48964 KiB, 23200 ms
# 14352.34495753338

# Analysis
# Closest pair returns slightly better results at the cost of much more time and space usage.
# I'll pass on coming up with my own heuristic, seeing as it already took a while to implement these two.
