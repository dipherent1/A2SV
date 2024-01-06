class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_val = sum(nums[:k])
        max_sum = sum_val
        for i in range(k, len(nums)):
            sum_val = sum_val - nums[i - k] + nums[i]
            max_sum = max(max_sum, sum_val)
        return max_sum / k