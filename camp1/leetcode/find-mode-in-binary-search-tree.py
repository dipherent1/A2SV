# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        ans = []
        
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            count[root.val]+=1
            helper(root.right)
        
        helper(root)
        m = max(count.values())
        for key,val in count.items():
            if val == m:
                ans.append(key)
        
        return ans