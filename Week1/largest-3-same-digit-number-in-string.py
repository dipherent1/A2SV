class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                # print(num[i:i+3])
                ans.append(int(num[i:i+3]))
            
        if len(ans) == 0:
            return ""
        elif max(ans) == 0:
            return "000"
        else:
            return str(max(ans))
        