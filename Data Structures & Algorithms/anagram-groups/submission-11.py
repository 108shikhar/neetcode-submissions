class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i,j in enumerate(strs):
            s=''.join(sorted(strs[i]))
            key=s
            if key not in d:
                d[key]=[]
            d[key].append(strs[i])
        a=[]
        for key, values in d.items():
            a.append(values)
        return a

