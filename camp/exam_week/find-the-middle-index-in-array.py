class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [nums[0]]
        suff_sum = [nums[-1]]
        for i in range(1,len(nums)):
            pre_sum.append(pre_sum[-1]+nums[i])
        for i in range(len(nums)-2,-1,-1):
            suff_sum.append(suff_sum[-1]+nums[i])
        print(pre_sum)
        print(suff_sum)
        l,r = 0,len(nums)-1
        for i in range(len(nums)):
            if pre_sum[i] == suff_sum[len(nums)-1-i]:
                return i
        return -1
        