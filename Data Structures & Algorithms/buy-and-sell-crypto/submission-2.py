class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,ans=0,1,0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
                r=r+1
            else:
                val=prices[r]-prices[l]
                ans=max(ans,val)
                r=r+1
        return ans
