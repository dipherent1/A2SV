class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = float('inf')
        sums = 0

        for r in range(len(nums)):
            sums+=nums[r]
            while l<=r and sums>=target:

                ans = min(ans,r-l+1)
                sums-=nums[l]
                l+=1
        return 0 if ans == float("inf") else ans
