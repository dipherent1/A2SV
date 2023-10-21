class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rs = 0
        ans = 0
        pairs = {0:0}
        for num in nums:
            rs+=num
            r = rs%k
            if r in pairs:
                pairs[r]+=1
                ans+=pairs[r]
            else:
                pairs[r] = 0
        return ans