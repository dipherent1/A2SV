class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        change = [0]*(len(s)+1)
        ans = ""
        for shift in shifts:
            p1, p2, dr = shift
            d = -1 if dr == 0 else 1
            change[p1]+=d
            change[p2+1]-=d
        print(change)
        for i in range(1,len(s)):
            change[i]+=change[i-1]
        print(change)
        for i in range(len(s)):
            ans+=(chr((ord(s[i])-97+change[i])%26+97))
        return(ans)