class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        p,a=set(),set() #p=pacific #a=atlantic
        def dfs(r,c,dictionary,previous):
            if (r<0 or r>=row) or (c<0 or c>=col):
                return
            elif heights[r][c] < previous or (r, c) in dictionary:
                return
            else:
                dictionary.add((r,c))
                for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    dfs(x,y,dictionary,heights[r][c])
        for c in range(col):
            dfs(0,c,p,heights[0][c])
            dfs(row-1,c,a,heights[row-1][c])
        for r in range(row):
            dfs(r,0,p,heights[r][0])
            dfs(r,col-1,a,heights[r][col-1])
        res=[]
        for r in range(row):
            for c in range(col):
                if ( (r,c) in p ) and ( (r,c) in a ):
                    res.append([r,c])
        return res