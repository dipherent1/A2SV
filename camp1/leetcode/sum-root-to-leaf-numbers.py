# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode],num=0) -> int:

        if root.left == None and root.right == None:
            num = num*10+root.val
            print(num)
            return num
        
        num = num*10+root.val
        val1 = val2 = 0

        if root.left:
            val1 = self.sumNumbers(root.left,num)
        
        if root.right:
            val2 = self.sumNumbers(root.right,num)
        
        # print(val1+val2,"sth")
        return val1+val2