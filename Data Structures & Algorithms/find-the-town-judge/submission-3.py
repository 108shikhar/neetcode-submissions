class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj=[[] for x in range(n+1)]
        adj[0].append(0)
        for m in trust:
            u,v=m[0],m[1]
            adj[u].append(v)
        inn=[0]*(n+1)
        for p in range(len(adj)):
            for q in adj[p]:
                inn[q]=inn[q]+1
        for i in range(len(adj)):
            j=adj[i]
            if len(j)==0 and inn[i]==(n-1):
                return i
        return -1