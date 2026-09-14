class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={0:1}
        for x in nums:
            ans={}
            for key,value in dp.items():
                s1=key-x
                s2=key+x
                if s1 not in ans:
                    ans[s1]=value
                elif s1 in ans:
                    ans[s1]=ans[s1]+value
                if s2 not in ans:
                    ans[s2]=value
                elif s2 in ans:
                    ans[s2]=ans[s2]+value
            dp=ans
        return dp.get(target,0)