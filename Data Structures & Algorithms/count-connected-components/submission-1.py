class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for x in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=[False]*n
        res=0
        def dfs(v):
            visit[v]=True
            for n in adj[v]:
                if visit[n]==False:
                    dfs(n)
        for i in range(len(adj)):
            if visit[i]==False:
                res=res+1
                dfs(i)
        return res