class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        r = len(s)//k
        count=0
        i = 0
        while i+k <= len(s):
            d = int(s[i:i+k])
            if d == 0:
                i+=1
                continue
            if num%d == 0:
                count+=1
            i+=1
        return count