class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char!= "]":
                stack.append(char)
            else:
                curstr = ""
                while stack and stack[-1]!="[":
                    curstr = stack.pop()+curstr
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop()+digit
                stack.append(curstr*int(digit))
        return "".join(stack)