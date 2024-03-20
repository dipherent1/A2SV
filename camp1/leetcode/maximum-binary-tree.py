# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        lefts = defaultdict(list)

        for i in range(len(nums)):
            
            while stack and stack[-1]<nums[i]:
                lefts[nums[i]].append(stack.pop())

            stack.append(nums[i])
        
        for key,val in lefts.items():
            lefts[key] = lefts[key][::-1]
        
        print(stack)
        print(lefts)
        # i = 0
        
        def build(arr,i):

            if arr == []:
                return None
            if i == len(arr):
                return None

            # for i in range(len(arr)):
            
            if arr[i] in lefts:
                left = build(lefts[arr[i]],0)
            else:
                left = None
            

            right = build(arr,i+1)

            
            return TreeNode(arr[i],left,right)
        
        return build(stack,0)

                
                
            
            
