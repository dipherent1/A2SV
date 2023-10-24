class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = current_min = 0
        overall_max = overall_min = nums[0]
        total= 0
        for num in nums:
            total+=num
            current_max = max(current_max+num, num)
            current_min = min(current_min+num, num)
            overall_max = max(current_max, overall_max)
            overall_min = min(current_min, overall_min)
        print(overall_max)
        print(overall_min)
        print(total)
        return max(overall_max,total-overall_min) if overall_max > 0 else max(nums)