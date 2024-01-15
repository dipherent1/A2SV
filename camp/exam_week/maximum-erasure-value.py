class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sums = 0
        seen =  set()
        l = 0
        ans = 0

        for r in range(len(nums)):
            
            while seen and nums[r] in seen:
                seen.remove(nums[l])
                sums -= nums[l]
                l+=1
            
            sums+=nums[r]
            ans = max(ans,sums)
            seen.add(nums[r])
        return ans
        