class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        lst = []
        while i < len(s)-2:
            if s[i+2] == "#":
                lst.append(s[i:i+2])
                i+=2
            else:
                lst.append(s[i])
            i+=1
        while i<len(s):
            lst.append(s[i])
            i+=1
        print(lst)
        ans = ""
        for num in lst:
            ans+=chr(int(num)+96)
        return ans