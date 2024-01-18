class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        "LOL, u tot"
        
        check = defaultdict(int)
        check[0]+=1
        ans = 0
        rs = 0
        
        for num in nums:
            rs +=num
            if rs-k in check:
                ans+=check[rs-k]
            check[rs]+=1
        return ans