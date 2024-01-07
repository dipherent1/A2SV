class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name+="1"
        typed+="1"
        count1 = 0
        count2 = 0
        p1 = 0
        ls1 = []
        ls2 = []
        temp = ""
        for i in range(len(name)-1):
            # count1+=1
            temp+=name[i]

            if name[i]!=name[i+1]:
                ls1.append(temp)
                temp = ""

        temp = ""
        for i in range(len(typed)-1):
            temp+=typed[i]
            if typed[i]!=typed[i+1]:
                ls2.append(temp)
                temp = ""

        if len(ls1)!=len(ls2):
            return False
        for i in range(len(ls1)):
            if len(ls1[i])>len(ls2[i]) or ls1[i][0]!=ls2[i][0]:
                return False
        return True
