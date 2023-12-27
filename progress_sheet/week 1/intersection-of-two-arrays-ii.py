class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        count2 = Counter(nums2)
        ans = []
        for key,val in count2.items():
            if key in count:
                ans.extend([key]*min(count[key],count2[key]))
        return ans

        