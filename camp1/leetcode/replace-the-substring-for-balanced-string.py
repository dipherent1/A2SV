class Solution:
    def balancedString(self, s: str) -> int:
        "QWER"
        def idx (key):
            if key == "Q":
                return 0
            if key == "W":
                return 1
            if key == "E":
                return 2    
            if key == "R":
                return 3

        count = Counter(s)
        k = len(s)//4
        extras = [0,0,0,0]
        extra_letters = set()
        for key,val in count.items():
            if val>k:
                extra_letters.add(key)
                extras[idx(key)] = val-k
            
        if all(val==0 for val in extras):
            return 0
        
        l = 0
        ans = float("inf")
        size = 0

        for r in range(len(s)):
            if s[r] in extra_letters:
                extras[idx(s[r])]-=1
            
            while l<=r and all(val<=0 for val in extras):
                ans = min(ans,r-l+1)
                if s[l] in extra_letters:
                    extras[idx(s[l])]+=1
                l+=1


        print(count)
        return ans
        