class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0]*(n+1)
        ls = list(s)
        ans = ""
        for start, end, c in shifts:
            if c == 1:
                k = 1
            else:
                k=-1
            prefix_sum[start]+=k
            prefix_sum[end+1]-=k
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1]+prefix_sum[i]

        for i in range(n):
            ls[i]=(chr((ord(ls[i])-97+prefix_sum[i])%26+97))

        return "".join(ls)

        