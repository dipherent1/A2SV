class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1]*n

        for i in range(2*n):
            j = i%n
            while stack and nums[stack[-1]] < nums[j]:
                ans[stack.pop()] = nums[j]
            stack.append(j)
        return ans
