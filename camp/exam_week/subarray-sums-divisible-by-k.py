class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        check = defaultdict(int)
        check[0]+=1
        rs = 0
        ans = 0

        for num in nums:
            rs+=num
            if rs%k in check:
                ans+=check[rs%k]
            check[rs%k]+=1
        return ans
        