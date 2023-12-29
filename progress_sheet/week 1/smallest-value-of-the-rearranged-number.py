class Solution:
    def smallestNumber(self, num: int) -> int:
        positive = False
        # ans = 0
        
        if num>0:
            positive = True

        if positive:
            arr = [int(digit) for digit in str(num)]
            arr.sort()
            i = 0
            while arr[i]==0:
                i+=1
            arr[i],arr[0] = arr[0],arr[i]
            ans = 0
            for num in arr:
                ans = ans*10 + num
            return ans

        else:
            arr = [int(digit) for digit in str(num)[1:]]
            arr.sort(reverse=True)
            ans = 0
            for num in arr:
                ans = ans*10 + num
            return ans*-1
       