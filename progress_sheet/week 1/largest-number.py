class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if int(str(nums[j])+str(nums[j+1])) < int(str(nums[j+1])+str(nums[j])):
                    # print("this")
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        nums = list(map(str,nums))
        ans =  str(int("".join(nums)))
        return ans