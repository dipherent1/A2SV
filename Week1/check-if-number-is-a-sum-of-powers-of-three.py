class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # print(n//3)
        reminder = 0
        while n > 0:
            reminder = n%3
            print(reminder,"re")
            n = int(n/3)
            print(n)
            if n == 2 or reminder == 2:
                return False
        return True
        