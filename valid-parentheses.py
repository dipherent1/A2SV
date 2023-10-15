class Solution:
    def isValid(self, s: str) -> bool:
        op = ["(","[","{"]
        cl = [")","]","}"]
        # if len(s) == 1:
        #     return False
        stack = []
        for ch in s:
            if ch in cl:
                if not stack:
                    return False
                cur = stack.pop()
                if op.index(cur)!=cl.index(ch):
                    return False
            elif ch in op: stack.append(ch)
        if not stack:
            return True
        else:
            return False