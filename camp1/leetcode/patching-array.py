class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        val = 0
        i = 0
        count = 0

        while i<len(nums) and val<n:
            
            if val+1 < nums[i]:
                count+=1
                temp = val + 1
                val+=temp
            
            else:
                val+=nums[i]
                i+=1
        
        while val<n:
            count+=1
            temp = val+1
            val+=temp
        return count 