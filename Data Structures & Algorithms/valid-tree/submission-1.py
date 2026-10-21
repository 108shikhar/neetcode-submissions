class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vertex=n
        adj=[[]for v in range(vertex)]
        for source, node in edges:
            adj[source].append(node)
            adj[node].append(source)
        res=0
        visit=[False]*len(adj)
        def dfs(v):
            visit[v]=True
            for n in adj[v]:
                if visit[n]==False:
                    dfs(n)
        for v in range(len(adj)):
            if visit[v]==False:
                res=res+1
                dfs(v)
        return True if res==1 and len(edges)==(n-1) else False