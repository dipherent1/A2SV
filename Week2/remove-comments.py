class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        i = 0
        ans = []
        while i <len(source):
            j = 0
            temp = ""
            while j<len(source[i]):
                if source[i][j] == "/":
                    
                    if j<len(source[i])-1 and source[i][j+1] =="/": #check //
                        break

                    elif j<len(source[i])-1 and source[i][j+1] =="*": #check if /*
                        j+=2
                        while not (j < len(source[i])-1 and source[i][j] == "*" and source[i][j+1] == "/"):#loops till it finds "*/"
                            
                            if j >= len(source[i])-2:#go to next line
                                i+=1
                                j = 0
                            else:
                                j+=1

                        j+=1 #since the while loop will end when j = * and j+1 = / 

                    else:#checks if its only "/"
                        temp+=source[i][j]

                else:
                    temp+=source[i][j]

                j+=1
            if temp:
                ans.append(temp) 
            i+=1

        return ans
