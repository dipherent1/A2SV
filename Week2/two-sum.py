class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # ans = [0,0]
        for i in range(len(nums)):
            if -nums[i] in dic:
                return [dic[-nums[i]],i]
            dic[nums[i]- target] = i
        