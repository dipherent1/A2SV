class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = 0
        stack = [[-2,-1]]
        heights.append(-1)
        min_for = defaultdict(int)
        ans = 0

        for r in range(len(heights)):
            
            while stack and stack[-1][0]>heights[r]:
                
                val,i = stack.pop()
                
                ans = max(ans,val*((r-i-1)+(i-stack[-1][1])))
            
            stack.append([heights[r],r])
        
        # for key,val in min_for.items():
        return ans