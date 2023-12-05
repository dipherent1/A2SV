class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        str1 = "qwertyuiopQWERTYUIOP"
        str2 = "asdfghjklASDFGHJKL"
        str3 = "zxcvbnmZXCVBNM"
        ans = []
        for word in words:
            count1 = 0
            count2 = 0
            count3 = 0
            for letter in word:
                if letter in str1:
                    count1+=1
                elif letter in str2:
                    count2+=1
                else:
                    count3+=1
            if count1 == len(word) or count2 == len(word) or count3 == len(word):
                ans.append(word)
        return ans

        