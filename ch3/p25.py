# 10 is the bin size
# asserter(lambda: bin_pack_best_fit([5, 6, 3]), [[5], [6, 3]])  # fit em as tight as poss
# asserter(lambda: bin_pack_worst_fit([5, 6, 3]), [[5, 3], [6]])  # loose as poss
"""
Brute force:
For each element, check each bin (implemented via array) for remaining size. Time: O(n^2), because
with n elements there can be at most n bins.

Approach 2:
Like above, but keep bins sorted in a BST. For each element, finding the partially filled bin that has the least room
but can still fit the element. O(lg n). Then reinsert that bin to preserve order. O(lg n). Total time: O(n lg n)

Approach 3:
Above approach can't work because of possibility of dupes in the BST. Instead we use priority queue (implemented 
as min-heap). It can't find the next tightest bin reliably though, so we need to be okay with the lack of guarantee.
Total time: O(n lg n)

Approach 4:
"""
