class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rs =0 
        res = max(nums)
        for num in nums:
            if rs<0:
                rs = 0
            rs+=num
            res = max(res,rs)
        return res