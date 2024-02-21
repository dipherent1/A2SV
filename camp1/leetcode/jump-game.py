class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_ind = 0
        for i in range(len(nums)):
            last_ind = max(last_ind,nums[i]+i)
            if i == last_ind:
                if  i == len(nums)-1:
                    return True
                return False
        return True
