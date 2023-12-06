class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)/3
        counter = Counter(nums)
        ans = []
        # print(count)
        for item,count in counter.items():
            if count>l:
                ans.append(item)
        return ans
        # for i in range(len(nums))