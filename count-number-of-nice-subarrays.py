class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        map = {0:1}
        rs = 0
        for num in nums:
            num = 0 if num%2 == 0 else 1
            rs +=num
            if rs - k in map:
                count+=map[rs-k]
            map[rs] = 1+map.get(rs,0)
        return count