class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        curr_max = float("-inf")
        area = 0
        while i < j and i < len(height):
            area = (j-i)*min(height[i],height[j])
            curr_max = max(curr_max,area)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return curr_max