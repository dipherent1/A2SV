class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        
        for i in range(len(height)):
            max_val = 0
            
            while stack and height[stack[-1]]<=height[i]:
                ind = stack.pop()
                
                ans+=(min(height[ind],height[i])-max_val)*(i-ind-1)
                
                max_val =max(max_val,height[ind])
            
            if len(stack)>=1:
                ans+=(height[i]-max_val)*(i-stack[-1]-1)
            
            stack.append(i)
        
        return ans