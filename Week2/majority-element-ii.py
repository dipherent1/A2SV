class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        for key,val in count.items():
            if val>len(nums)/3:
                ans.append(key)
        return ans
