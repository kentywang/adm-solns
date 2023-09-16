# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
cases:
- √ same node => immediately return either of them
- √ one node is ancestor of another => if one node's value is the current node's value and the other isn't, that node is the LCA
- √ nodes share different common ancestor => LCA is node where subtree to search differs between nodes

"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if one of the nodes is the current, we know that's the LCA
        while True:
            if p.val == root.val or q.val == root.val or p.val < root.val < q.val or p.val > root.val > q.val:
                return root
            root = root.left if p.val < root.val else root.right
