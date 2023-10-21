class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and (i-ans)%2 == 0:
                ans+=1
        return ans + (len(nums)-ans)%2