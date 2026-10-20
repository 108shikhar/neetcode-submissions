class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for c in range(numCourses)]
        for x in prerequisites:
            curr,pre=x[0],x[1]
            adj[pre].append(curr)
        q,ans=deque(),[]
        inn=[0]*len(adj)
        for i in range(len(adj)):
            for j in adj[i]:
                inn[j]=inn[j]+1
        for x in range(len(inn)):
            if inn[x]==0:
                q.append(x)
        while q:
            val=q.popleft()
            ans.append(val)
            for x in adj[val]:
                inn[x]=inn[x]-1
                if inn[x]==0:
                    q.append(x)
        return ans if len(ans)==numCourses else []