class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l] == val:
                nums[l] = nums[r]
                r-=1
            else:
                l+=1

        return l