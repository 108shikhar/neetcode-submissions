class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[i]>temperatures[stk[-1]]:
                j=stk.pop()
                ans[j]=i-j
            stk.append(i)
        return ans
