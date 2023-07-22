"""
(a)
    Each node needs 16 bytes (4 for data, 4 for each child pointer, and 4 for parent). The ratio is 1/4.
    Each node needs to reserve those 16 bytes, even if there may be no parent (e.g root) or children (e.g. leaf),
    so the ratio doesn't change for n nodes.
(b) For a single node, 4 bytes are for data and 4 are for child pointers (1/2). For two nodes, the parent is 4 bytes of
    pointers, while the child is 4 bytes for data and 4 for pointers (1/3). For three nodes (of a balanced BST), that
    becomes 2/5. For 7 nodes (balanced), 3 will be "internal" nodes of 4 bytes each, while the 4 leaves are 8 bytes, 4
    of which are pointers (4/11).
    In general, for balanced trees, a little more than half will be leaves, and a little less than half will be internal,
    meaning ~n/2 have 4/8 and ~n/2 will have 0/4, summing 2n data bytes and (2n + 2n) pointer bytes, for a 2/6 = 1/3 ratio.
    For the most unbalanced tree, a linked list, n-1 nodes will be 0/4, while 1 node will be 4/8, for a total of 4 data
    bytes and 4n pointer bytes, an efficiency ratio of 1/(n+1), meaning it's most efficient at 1/2 with 1 node and gets
    very unefficient at 1/100 at 99 nodes and so forth.

    If the situation in (a) needed 2 bytes instead of 4 for each pointer, its ratio would be 2/5 (40%) and would
    compare favorably against the 1/3 (33%) for the best-case of (b). If no parent pointers were needed too, that would
    make (a) even better at 1/2 (50%).
"""
