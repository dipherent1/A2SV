class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5:0 , 10:0}
        for val in bills:
            if val == 5:
                coins[5]+=1
            else:
                if coins[5] == 0:
                    return False
                    
                if val == 10:
                    coins[5]-=1
                    coins[10]+=1
                else:
                    if coins[10]:
                        coins[10]-=1
                        coins[5]-=1
                    else:
                        if coins[5]>=3:
                            coins[5]-=3
                        else:
                            return False
        return True