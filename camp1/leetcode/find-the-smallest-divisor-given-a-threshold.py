class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def checker(val):
            return sum([ceil(num / val) for num in nums])
            # return sums<=threshold
        
        l = 1
        r = max(nums)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            val = checker(mid)
            
            # if val == threshold:
            #     return mid
            
            if val<=threshold:
                ans = mid
                
                print(mid,val)
                
                r = mid-1
            else:
                l = mid+1
        return ans