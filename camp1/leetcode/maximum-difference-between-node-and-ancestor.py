# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode],cur_max = float("-inf"),cur_min = float("inf"), diff = 0 ) -> int:
        if not root:
            return cur_max - cur_min
        
        cur_max = max(cur_max,root.val)
        cur_min = min(cur_min,root.val)
        
        left = self.maxAncestorDiff(root.left,cur_max,cur_min,diff)
        right = self.maxAncestorDiff(root.right,cur_max,cur_min,diff)

        diff = max([diff,left,right])
        return diff

