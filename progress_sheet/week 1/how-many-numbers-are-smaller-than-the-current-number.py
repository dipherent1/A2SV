class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls = sorted(nums)
        ans = [0]*len(nums)
        dic = {}
        for i in range(len(ls)):
            if ls[i] not in dic:
                dic[ls[i]] = i
        for i in range(len(nums)):
            ans[i] = dic[nums[i]]
        return ans