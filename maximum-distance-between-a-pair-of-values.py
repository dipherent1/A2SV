class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        while i<len(nums1) and j<len(nums2):
            if i>j or nums1[i]>nums2[j]:
                i+=1
            ans = max(ans,j-i)
            j+=1
        return ans