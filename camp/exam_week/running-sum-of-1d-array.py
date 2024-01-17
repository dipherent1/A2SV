class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        rs = 0
        for num in nums:
            rs+=num
            ans.append(rs)
        return ans