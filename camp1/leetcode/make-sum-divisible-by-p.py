class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        k = tot%p
        
        rs = 0
        ans = float("inf")
        mp = {0:-1}
        
        if k == 0:
            return 0

        for r in range(len(nums)):
            rs+=nums[r]

            if (rs-k)%p in mp:
                ans = min(ans,r-mp[(rs-k)%p])

            mp[rs%p] = r
        
        return ans if ans < len(nums) else -1