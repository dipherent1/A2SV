# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            mid = (l+r)//2
            if l>r:
                return None
            return TreeNode(nums[mid],helper(l,mid-1),helper(mid+1,r))
        return helper(0,len(nums)-1)