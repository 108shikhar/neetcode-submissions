class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for c in range(numCourses)]
        for i in prerequisites:
            curr,pre=i[0],i[1]
            adj[pre].append(curr)
        inn=[0]*numCourses
        q=deque()
        for i in range(len(adj)):
            for j in adj[i]:
                inn[j]=inn[j]+1
        for x in range(numCourses):
            if inn[x]==0:
                q.append(x)
        count=0
        while q:
            val=q.popleft()
            count=count+1
            for c in adj[val]:
                inn[c]=inn[c]-1
                if inn[c]==0:
                    q.append(c)
        return True if count==numCourses else False