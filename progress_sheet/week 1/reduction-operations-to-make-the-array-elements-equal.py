class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == nums[i+1]:
                continue
            ans+=len(nums)-1-i
        return ans    
        