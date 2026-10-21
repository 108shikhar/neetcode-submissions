class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans=[False]*len(queries)
        adj=[[] for c in range(numCourses)]
        reach=[set() for c in range(numCourses)]
        for before, after in prerequisites:
            adj[before].append(after)
        inn=[0]*numCourses
        for i in range(len(adj)):
            for j in adj[i]:
                inn[j]=inn[j]+1
        q,topo=deque(),[]
        for i in range(len(inn)):
            if inn[i]==0:
                q.append(i)
        while q:
            val=q.popleft()
            topo.append(val)
            for n in adj[val]:
                inn[n]=inn[n]-1
                if inn[n]==0:
                    q.append(n)
        for c in reversed(topo):
            for n in adj[c]:
                reach[c].add(n)
                reach[c].update(reach[n])
        for i, v in enumerate(queries):
            before, after=v[0],v[1]
            if after in reach[before]:
                ans[i]=True
        return ans