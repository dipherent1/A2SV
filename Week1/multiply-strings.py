class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        num2 = num2[::-1]
        num1 = num1[::-1]
        for i,val1 in enumerate(num2):
            temp = ""
            carry = 0
            for j,val2 in enumerate(num1):
                pro = int(val1)*int(val2)
                if carry:
                    pro+=carry
                    carry = 0
                if pro>9:
                    carry = pro//10
                    pro = pro%10
                temp=str(pro)+temp
            if carry:  # Add the remaining carry
                temp=str(carry)+temp
            ans += int(temp)*(10**i)
        return str(ans)
