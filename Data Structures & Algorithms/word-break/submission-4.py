class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m=len(s)+1
        dp=[False]*m
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                j=len(w)
                if s[i:i+j]==w:
                    dp[i]=dp[i+j]
                if dp[i]==True:
                    break
        return dp[0]