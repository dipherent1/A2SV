class Solution:
    def simplifyPath(self, path: str) -> str:
        path = (path).split("/")
        stack = []
        ans = ""
        print(path)
        for c in path:
            if c == "." or c == "":
                continue
                
            if c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        print(stack)
        # stack = stack.strip("")
        for ch in stack:
            if ch != "":
                ans+="/"+ch

        return ans if ans != "" else "/"