class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        l = 0
        ans = ""
        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack and s[stack[-1]] =="(" :
                    stack.pop()
                else:
                    stack.append(i)
        for i in range(len(s)):
            if l < len(stack) and i == stack[l]:
                l+=1
                continue
            ans+=s[i]
        return ans