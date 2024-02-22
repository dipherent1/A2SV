class Solution:
    def isValid(self, s: str) -> bool:
        op = ["(","[","{"]
        cl = [")","]","}"]
        stack  = []

        for c in s:
            if c in op:
                stack.append(c)
            if c in cl:
                if not stack:
                    return False
                if op.index(stack[-1]) == cl.index(c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
