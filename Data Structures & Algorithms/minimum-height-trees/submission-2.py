class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj=[[] for i in range(n)]
        for one, two in edges:
            adj[one].append(two)
            adj[two].append(one)
        deg=[len(adj[i]) for i in range(n)]
        q=deque()
        for i in range(n):
            if deg[i]==1:
                q.append(i)
        while n>2:
            size=len(q)
            n=n-size
            for val in range(size):
                vertex=q.popleft()
                for node in adj[vertex]:
                    deg[node]=deg[node]-1
                    if deg[node]==1:
                        q.append(node)
        return list(q)