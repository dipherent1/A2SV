class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                cur = 0
                while stack[-1] != "(":
                    cur+=stack.pop()
                stack.pop()
                if cur == 0:
                    stack.append(1)
                else:
                    stack.append(cur*2)
        while len(stack)>1:
            stack.append(stack.pop()+stack.pop())
        return stack[-1]