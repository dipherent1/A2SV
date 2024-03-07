# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def check(val):
            return low<=val<=high
        
        ans = 0
        
        def helper(root):
            nonlocal ans
            if not root:
                return 
            
            if check(root.val):
                ans+=root.val
            
            helper(root.left)
            helper(root.right)
        
        helper(root)                
        return ans
        