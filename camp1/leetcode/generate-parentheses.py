class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opens = ["("]*n
        closes = [")"]*n
        ans = []
        
        def isvalid(path):
            stack = []
            for ch in path:
     
                if ch == ")":
                    if not stack:
                        return False
                        
                    stack.pop()
                else:
                    stack.append(ch)
            
            return not stack
        
        def helper(path,o,c):
            
            if len(path) == 2*n:
                # if isvalid(path):
                ans.append("".join(path))
                return 

            if o<n:
                
                path.append("(")
                helper(path,o+1,c) 
                path.pop()               
            if o and o>c:
                path.append(")") 
                helper(path, o,c+1)
                path.pop()
  
        helper([],0,0)
        return ans