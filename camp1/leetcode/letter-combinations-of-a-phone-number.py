class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        ind = 0
        if not digits:
            return []

        def helper(i,path):
            if len(path) == len(digits):
                ans.append("".join(path))
            
            for j in range(i,len(digits)):
                letters = buttons[digits[j]]
                for k in range(len(letters)):
                    path.append(letters[k])
                    helper(j+1,path)
                    path.pop()
            
        helper(0,[])
        return ans

