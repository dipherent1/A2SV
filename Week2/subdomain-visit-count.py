class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        res = []
        for i in cpdomains:
            rep, d = i.split()
            dr =d.split(".")
            big=0
            while big < len(dr):
                if  ".".join(dr[big:]) in dic:
                    dic[".".join(dr[big:])] +=int(rep)

                else:
                    dic[".".join(dr[big:])] = int(rep) 
                big+=1
        for key,value in dic.items():
            res.append(f"{value} {key}")
        return res
