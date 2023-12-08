class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}
        for cp in cpdomains:
            num,domains = cp.split(" ")
            # domains = domains.split(".")
            mp[domains] = mp.get(domains,0)+int(num)
            for i in range(len(cp)-1,-1,-1):
                if cp[i] == ".":
                    mp[cp[i+1:]] = mp.get(cp[i+1:],0)+int(num)
        ans = []
        # print(mp)
        for key, values in mp.items():
            ans.append(f"{values} {key}")
        return ans



        