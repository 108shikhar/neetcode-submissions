class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #dsu=union+find
        n=len(edges)
        parent=[i for i in range(n+1)] #every node is parent to itself
        rank=[1]*(n+1) #rank means ki ek node kitne nodes ka parent hai
        #dsu is first unite then find unity if exists
        def find(n):
            if n!=parent[n]:
                parent[n]=find(parent[n])
            return parent[n]
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]=rank[p1]+rank[p2]
            else:
                parent[p1]=p2
                rank[p2]=rank[p2]+rank[p1]
            return True
        for n1,n2 in edges:
            if union(n1,n2) is False:
                return [n1,n2]
