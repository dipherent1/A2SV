class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        running_sum = 0
        total = sum(nums)
        for i in range(len(nums)):
            post_sum = total-running_sum-nums[i]
            if running_sum == post_sum:
                return i
            running_sum+=nums[i]
        return -1