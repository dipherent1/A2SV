class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = sum(nums)+1
        summ = 0
        l = 0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target and l<=r:
                summ -= nums[l]
                ans = min(ans,r-l+1)
                l+=1
                
        return 0 if ans == sum(nums)+1 else ans