class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""
        string2 = ""
        for word in word1:
            for letter in word:
                string1+=letter
        for word in word2:
            for letter in word:
                string2+=letter
        return string1 == string2