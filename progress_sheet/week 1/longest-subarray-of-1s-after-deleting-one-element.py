class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        count = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count+=1
            while l<r and count>1:
                if nums[l] == 0:
                    count-=1
                l+=1
            # print(r-l+1-count)
            ans = max(ans,r-l)
        return ans