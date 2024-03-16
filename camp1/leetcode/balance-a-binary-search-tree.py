# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def parser (root):
            if not root:
                return 
            
            arr.append(root.val)
            
            parser(root.left)
            
            parser(root.right)
        
        parser(root)

        # ans = TreeNode()
        
        arr.sort()
        
        l = 0
        r = len(arr)-1

        def bst(l,r):
            if l>r:
                return 
            mid = (l+r)//2
            return TreeNode(arr[mid], bst(l,mid-1), bst(mid+1,r))
        return bst(l,r)
