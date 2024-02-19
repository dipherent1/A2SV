class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        rs = 0
        
        for i in range(len(nums)):
            rs+=nums[i]
            if rs<0:
                rs = 0
            ans = max(rs,ans)
        return max(nums) if ans == 0 else ans
        