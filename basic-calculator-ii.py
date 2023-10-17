class Solution:
    def calculate(self, s: str) -> int:
        def arthemetic(nums1,nums2,op):
            if op == "+":
                return nums1+nums2
            if op == "-":
                return nums1-nums2

        nums = []
        op = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
            
                cur_num = 0
                while i < len(s) and s[i].isdigit():
                    cur_num = cur_num * 10 + int(s[i])
                    i += 1
                nums.append(cur_num)
                i-=1
            else:
                o = s[i]
                while not s[i].isdigit():
                    i+=1
                cur_num = 0
                while i < len(s) and s[i].isdigit():
                    cur_num = cur_num * 10 + int(s[i])
                    i += 1
                i-=1
                if o == "+":
                    nums.append(cur_num)
                    op.append(o)
                elif o == "-":
                    nums.append(-cur_num)
                elif o == "*":
                    nums[-1] = nums[-1] * cur_num
                elif o == "/":
                    nums[-1] = int(nums[-1] / cur_num)
    
    
    
            i+=1
        print(nums)
        print(op)
        # while op:
        #     nums2 = nums.pop()
        #     nums1 = nums.pop()
        #     o = op.pop()
        #     nums.append(arthemetic(nums1,nums2,o))

        return(sum(nums))