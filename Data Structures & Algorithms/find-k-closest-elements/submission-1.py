class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d={}
        for i in range(0,len(arr),1):
            m=arr[i]
            n=abs(x-m)
            d[i]=n
        d=sorted(d.items(), key=lambda x: x[1])
        a=[]
        for j in range(0,k):
            a.append(arr[d[j][0]])
        a.sort()
        return a