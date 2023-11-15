class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        [10,5,2,6]
              r
            l
        '''
        l = 0
        ans = 0
        running_product = 1
        for r in range(len(nums)):
            running_product*=nums[r]
            while running_product >=k and l<=r:
                running_product/=nums[l]
                l+=1
            ans += r-l+1
        return ans