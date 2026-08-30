class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        for i in range(0,len(strs[0]),1):
            for j in range(1,len(strs),1):
                x=strs[j]
                if i>=len(x) or x[i]!=strs[0][i]:
                    return s
            s=s+strs[0][i]
        return s
            