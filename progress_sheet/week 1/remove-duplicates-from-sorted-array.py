class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ls = set()
        i = 0
        d = 0
        while i < len(nums): 
            while i<len(nums) and nums[i] in ls:
                i+=1
            if i  == len(nums):
                break
            nums[d] = nums[i]
            d+=1
            ls.add(nums[i])
            i+=1
        return d

