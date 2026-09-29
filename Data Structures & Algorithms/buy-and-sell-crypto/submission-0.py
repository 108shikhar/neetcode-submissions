class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(0,len(prices)-1,1):
            for j in range(i+1,len(prices),1):
                if prices[i]<prices[j]:
                    sell=prices[j]-prices[i]
                    ans=max(ans,sell)
        return ans