class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        ans = 0
        for r in range(len(nums)):
            total += nums[r]
            while total + k < nums[r] * (r - l + 1):
                total -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans