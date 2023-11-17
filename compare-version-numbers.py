class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        
        i = 0
        # j = 0
        while i<len(ver1) and i<len(ver2):
            if int(ver1[i]) == int(ver2[i]):
                pass
            elif int(ver1[i]) > int(ver2[i]):
                return 1
            else:
                return -1
            i+=1
            # j+=1
        while i<len(ver1):
            if int(ver1[i]) > 0:
                return 1
            i+=1
        while i<len(ver2):
            if int(ver2[i]) > 0:
                return -1
            i+=1
        
        
        return 0