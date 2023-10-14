class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        elif target == 0:
            return len(nums)
        
        l = 0
        s = 0
        res = -1
        for r in range(len(nums)):
            s += nums[r]
            while s > target:
                s -= nums[l]
                l += 1
            if s == target:
                res = max(res, r - l + 1)
        
        return -1 if res == -1 else len(nums) - res