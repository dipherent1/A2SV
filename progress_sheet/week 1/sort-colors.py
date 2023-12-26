class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i]+=1
        ans = []
        for i in range(len(count)):
            ans.extend([i]*count[i])
        for i in range(len(nums)):
            nums[i] = ans[i]
