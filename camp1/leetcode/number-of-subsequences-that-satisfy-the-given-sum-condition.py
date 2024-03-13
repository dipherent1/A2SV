class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        l = 0
        r = len(nums)-1
        
        ans = 0
        
        while l<=r:
            if nums[r]+nums[l]>target:
                r-=1
            
            else:
                print(r+1)
                ans+=(2**(r-l))%(10**9 + 7)

                l+=1
        
        return ans%(10**9+7)

