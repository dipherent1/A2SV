class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = {}
        stack = []
        ans = [-1]*len(nums1)

        for num in nums2:
            while stack and stack[-1] <num:
                check[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            if nums1[i] in check:
                ans[i] = check[nums1[i]]
        return ans