class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        for path in paths:
            # print (path)
            root_name,*file_names = path.split(" ")
            file_names = [*file_names]
            # print(file_names)
            for f in file_names:
                for i,char in enumerate(f):
                    if char == "(":
                        files[f[i:]].append(root_name+"/"+f[:i])
                        break
        print(files)
        ans = []
        for files in files.values():
            if len(files)>1:
                ans.append(files)
        return ans
            # print(root_name)
        #     root,name = root_name.split(" ")
        #     files[f].append([root+"/"+name+"."])
        # print(files)