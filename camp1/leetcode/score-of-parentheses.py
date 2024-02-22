class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack[-1] == "(":
                    stack[-1] = 1
                else:
                    cur = 0
                    while stack[-1] != "(":
                        cur+= stack.pop()
                    stack.pop()
                    stack.append(cur*2)
        print(stack)
        return sum(stack)
