"""
8:46 - 9:10 planning (24m)
 - 9:36     coding (25m)

# check for nodes in left.
    # if both nodes in left, their LCA should've bubbled up to us, so keep bubbl it
    # if 1 node, check right subtree for other node specifically
    #   if none, just return node 1 up
    #   if some, return self, since we're the LCA
    # if no nodes, return none

# dfs returns 1 node or the LCA, expects LCA to be bubbled, expect 1 node to be found the partner
# partner dfs returns sth or nothing

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        O(n) time, O(h) space

        dfs
        """

        def lca(curr):
            if not curr:
                return None, None

            rem_tgt, maybeLca = None, None

            if curr == p:
                rem_tgt = q
            if curr == q:
                rem_tgt = p

            if not rem_tgt:
                rem_tgt, maybeLca = lca(curr.left)
            # curr node is one node, check the trees
            else:
                if findNode(curr, rem_tgt):
                    return None, curr
                else:
                    return rem_tgt, None

            # subrecursion found LCA already, bubble up the answer
            if maybeLca:
                return None, maybeLca

            # no target nodes in left subtree
            if not rem_tgt:
                return lca(curr.right)

            # left found sth, so find partner
            if findNode(curr.right, rem_tgt):
                # curr is LCA!
                return None, curr

            # one node in left tree, other node not in right tree, so LCA is above us,
            # so bubble up work so far
            return rem_tgt, None

        def findNode(curr, tgt):
            if not curr:
                return False
            if curr == tgt:
                return True
            return findNode(curr.left, tgt) or findNode(curr.right, tgt)

        return lca(root)[1]


# Online solution that is amazingly elegant
# it does potentially traverse more of the tree though
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r
