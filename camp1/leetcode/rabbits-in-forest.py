class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        check = defaultdict(int)
        ans = 0
        for color in answers:
            check[color]+=1
        for key,val in check.items():
            if key == 0:
                ans+=val
            elif val <= key+1:
                ans+=key+1
            else:
                if val%(key+1) == 0:
                    x = val//(key+1)
                else:
                    x = (val//(key+1))+1
                print(x)
                ans+=(key+1)*x


        print(check)
        return ans
        