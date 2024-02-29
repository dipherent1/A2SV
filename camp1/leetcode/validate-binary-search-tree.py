# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],minn = float("inf"),maxx=float("-inf")) -> bool:
        if not root:
            return True
            
        if root.val>=minn or root.val<=maxx:
            return False

        left = self.isValidBST(root.left,root.val,maxx)
        
        right = self.isValidBST(root.right,minn,root.val)
        
        return left and right

        