class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = len(nums)-1
        l = 0
        while l<r:
            sum = nums[l]+nums[r]
            if sum > target:
                r-=1
            elif sum<target:
                l+=1
            else:
                return [l+1,r+1]

        