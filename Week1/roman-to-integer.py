class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
        # odds = ["I","X","C"]
        ans = numbers[s[0]]
        for i in range(1,len(s)):
            if (s[i] == "V" and s[i-1] == "I") or (s[i] == "X" and s[i-1] == "I"):
                ans-=numbers[s[i-1]]
                ans+=(numbers[s[i]] - numbers[s[i-1]])
            elif (s[i] == "L" and s[i-1] == "X") or (s[i] == "C" and s[i-1] == "X"):
                ans-=numbers[s[i-1]]
                ans+=(numbers[s[i]] - numbers[s[i-1]])
            elif (s[i] == "D" and s[i-1] == "C") or (s[i] == "M" and s[i-1] == "C"):
                ans-=numbers[s[i-1]]
                ans+=(numbers[s[i]] - numbers[s[i-1]])
            else:
                ans+=numbers[s[i]]
        return ans