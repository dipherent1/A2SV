class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        int_num = n
        while True:
            str_num = str(int_num)
            print(str_num)
            int_num = 0
            if str_num == "1":
                return True

            for num in str_num:
                int_num = int_num + int(num)**2
            
            if int_num not in check:
                check.add(int_num)
            else:
                return False
            # print(int_num)


        