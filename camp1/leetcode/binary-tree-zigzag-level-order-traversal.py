# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        height = defaultdict(list)
        depth = 0

        def helper(root,depth):
            if not root:
                return 
            
            height[depth].append(root.val)

            helper(root.left,depth+1)
            
            helper(root.right,depth+1)
        helper(root,depth)
        ans = []
        for i in range(len(height)):
            if i%2:
                ans.append(height[i][::-1])
            else:
                ans.append(height[i])
        return ans

