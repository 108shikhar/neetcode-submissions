class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[[[-1 for d in range(2)] for c in range(n)] for r in range(n)]
        def stone(l,r,k):
            if l>r:
                return 0
            if dp[l][r][k]!=-1:
                return dp[l][r][k]
            if k==0:
                a1=piles[l]+stone(l+1,r,1)
                a2=piles[r]+stone(l,r-1,1)
                alice=max(a1,a2)
            if k==1:
                b1=stone(l+1,r,0)
                b2=stone(l,r-1,0)
                alice=min(b1,b2)
            dp[l][r][k]=alice
            return dp[l][r][k]
        val=(sum(piles)//2)
        if stone(0,n-1,0)>val:
            return True
        else:
            return False