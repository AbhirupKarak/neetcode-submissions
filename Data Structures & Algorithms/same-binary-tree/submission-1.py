# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    Same = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        
        if p.val == q.val:
            self.Same = True
        else:
            return False
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            self.Same = True
        else:
            self.Same = False
        return self.Same