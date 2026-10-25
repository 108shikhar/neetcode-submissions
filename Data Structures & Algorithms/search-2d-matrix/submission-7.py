class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,h,a,b=0,len(matrix[0])-1,0,len(matrix[0])-1
        while l<=h and a<len(matrix):
            m=(l+h)//2
            if l<=b:
                if matrix[a][m]==target:
                    return True
                elif matrix[a][m]<target:
                    if l==b:
                        a=a+1
                        l,h=0,b
                    else:
                        l=m+1
                elif matrix[a][m]>target:
                    h=m-1
        return False
