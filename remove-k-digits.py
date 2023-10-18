class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for cur in num:
            while stack and k > 0 and cur < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(cur)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        # Remove leading zeros
        res = res.lstrip('0')
        return res if res else "0"