class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        for i in range(len(strs[0])):
            for j in strs:
                if i==len(j) or strs[0][i]!=j[i]:
                    return ans
            ans=ans+strs[0][i]
        return ans