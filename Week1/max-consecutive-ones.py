class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        ans = 0
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans,i-start)
                start = i+1
        return ans