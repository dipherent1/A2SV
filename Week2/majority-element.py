class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # max_val = 0
        max_key = 0
        count = Counter(nums)
        for key,val in count.items():
            if val>len(nums)/2:
                return key
        # return key
        