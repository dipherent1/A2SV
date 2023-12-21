class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)-1

        hold = 0
        while n>0:
            digits[n]+=(1)
            if digits[n]>9:
                digits[n]=0
                # hold = 1
            else:
                return digits
            n-=1
    
        if digits[0] == 9:
            digits[0] = 0
            return [1]+digits
        else:
            digits[n]+=(1)
            return digits