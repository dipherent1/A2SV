class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = ""
        while i < len(command)-1:
            if command[i] == "G":
                ans+="G"
                i+=1
            elif command[i] == "(" and command[i+1] == ")":
                ans+="o"
                i+=2
            elif command[i] == "(" and command[i+1] == "a":
                ans+="al"
                i+=4
        if command[-1] == "G":
            ans+="G"
        return ans
        