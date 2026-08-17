class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i, j in enumerate(strs):
            value=strs[i]
            key="".join(sorted(strs[i]))
            if key not in d:
                d[key]=[]
                d[key].append(value)
            elif key in d:
                d[key].append(value)
        l=list(d.values())
        return l