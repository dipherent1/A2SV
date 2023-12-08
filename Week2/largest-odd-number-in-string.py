class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = 0
        number = 0
        for i, digit in enumerate(num):
            # print(digit)
            # number = number*10+int(digit)
            if int(digit)%2 == 1:
                odd = num[:i+1]
        return "" if not odd else str(odd)