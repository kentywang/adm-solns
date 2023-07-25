"""
If elements in first BST are all smaller than elements in second BST, simply walk down left side of 2nd BST and add the
first BST as the leftmost child. Time: O(h) (h = height of 2nd tree)

If BSTs overlap in range, then I don't know if you can do it in log time, because it seems like you'd need to check
every node on both trees.
"""
