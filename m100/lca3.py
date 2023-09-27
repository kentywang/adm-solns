"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


Observations:


Cases:
- 2 nodes
-

Option 1: [time: O(h), space: O(h)]
- traverse to root for one node, saving each node in its path (including self) to hash set (space is O(h))
- traverse to root on other node, checking in each node if its on the path (h checks, O(1) per check)
- curr node is always the lowest possible ancestor, so corner case is covered. We'll never have an ancestor below curr, because we've already checked them.


Planning    14:15-14:28 (13 min)
Coding      14:25-14:33 (8 min)
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ppath = set()

        # make path to parent from one of the nodes, saving each node on the path
        while p:
            ppath.add(p)
            p = p.parent

        while q not in ppath:
            q = q.parent

        return q


"""
23:59 - 0:01 (2m)
"""


class Solution:
    def lowestCommonAncestor2(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q

        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p

        return a
