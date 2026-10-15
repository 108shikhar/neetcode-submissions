class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        val=[0]*(n+1)
        for x,y in trust:
            val[x]=val[x]-1
            val[y]=val[y]+1
        for i in range(len(val)):
            j=val[i]
            if j==(n-1):
                return i
        return -1