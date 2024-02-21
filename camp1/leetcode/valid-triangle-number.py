class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for r in range(len(nums)-1,-1,-1):
            l = 0
            m= r-1
            while m>l:
                if nums[l]+nums[m]>nums[r]:
                    count += m-l
                    m-=1
                else:
                    l+=1
                    
               
        return count 
            
        