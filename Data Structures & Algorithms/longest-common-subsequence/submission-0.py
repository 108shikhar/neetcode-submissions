class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)-1
        n=len(text2)-1
        dp=[[None for c in range(n+1)] for r in range(m+1)]
        def lcs(m,n):
            if m<0 or n<0:
                return 0
            if dp[m][n]!=None:
                return dp[m][n]
            if text1[m]==text2[n]:
                dp[m][n]=1+lcs(m-1,n-1)
            else:
                dp[m][n]=max(lcs(m-1,n),lcs(m,n-1))
            return dp[m][n]
        return lcs(m,n)