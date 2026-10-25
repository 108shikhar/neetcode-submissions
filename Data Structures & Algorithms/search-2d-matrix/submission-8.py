class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        top,bottom=0,row-1
        while top<=bottom:
            mid=(top+bottom)//2
            if matrix[mid][-1]<target:
                top=mid+1
            elif matrix[mid][0]>target:
                bottom=mid-1
            else:
                break
        if top>bottom:
            return False
        row=(top+bottom)//2
        l,h=0,col-1
        while l<=h:
            m=(l+h)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]<target:
                l=m+1
            elif matrix[row][m]>target:
                h=m-1
        return False