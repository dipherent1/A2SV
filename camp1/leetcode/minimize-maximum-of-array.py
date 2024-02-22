class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        rs = nums[0]
        for i in range(1,len(nums)):
            rs+=nums[i]
            ans = max(ans,ceil(rs/(i+1)))
        return ans
