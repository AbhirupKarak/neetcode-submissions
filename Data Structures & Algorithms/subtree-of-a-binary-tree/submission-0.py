# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            
            if p.val != q.val:
                return False

            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

        if isSameTree(root, subRoot):
            return True
        else:
            if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot):
                return True
        return False