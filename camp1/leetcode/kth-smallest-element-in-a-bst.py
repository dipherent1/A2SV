# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # min_val = float("inf")
        if  k == 0:
            return root.val
        
        cur = 0
        min_val = 0
        def traverse(root):
            
            nonlocal cur
            nonlocal min_val

            if not root:
                return

            
            traverse(root.left)
            cur+=1
            if k == cur:
                min_val = root.val
                return
            right = traverse(root.right)
            
            # cur+=1
            
        
        traverse(root)
        
        return min_val

