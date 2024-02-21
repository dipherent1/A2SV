class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        if all(palindrome[i] == palindrome[len(palindrome)-i-1] == "a" for i in range(len(palindrome)//2)):
            palindrome[-1] = "b"
            return "".join(palindrome)
        
        for i in range(len(palindrome)):
            if palindrome[i]!="a":
                palindrome[i] = "a"
                return "".join(palindrome)