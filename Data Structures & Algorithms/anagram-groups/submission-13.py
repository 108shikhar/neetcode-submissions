class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i, x in enumerate(strs):
            y="".join(sorted(x))
            if y not in d:
                d[y]=[]
                d[y].append(x)
            elif y in d:
                d[y].append(x)
        return list(d.values())