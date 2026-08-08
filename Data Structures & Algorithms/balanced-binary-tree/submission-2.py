# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    Balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        #we want to return the difference between left and right subtree of each node
        def height(root):
            leftHeight = 0
            rightHeight = 0
            if root is None:
                return 0
            leftHeight += height(root.left)
            rightHeight += height(root.right)
            if abs(leftHeight - rightHeight) > 1:
                self.Balanced = False
            return 1 + max(leftHeight,rightHeight)
        height(root)
        return True if self.Balanced else False

