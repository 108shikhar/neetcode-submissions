class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(0, len(prices)-1, 1):
            j=i+1
            x=prices[i]
            y=prices[j]
            if y>x:
                z=y-x
                profit=profit+z
        return profit
